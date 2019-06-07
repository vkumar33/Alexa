import random
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
AbstractRequestHandler, AbstractExceptionHandler,
AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response
from ask_sdk_model.dialog import (
    ElicitSlotDirective, DelegateDirective)
from ask_sdk_model import (
    Response, IntentRequest, DialogState, SlotConfirmationStatus, Slot)

sb = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



# Built-in Intent Handlers
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or
        is_intent_name("LaunchRequestIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        session_attr = handler_input.attributes_manager.session_attributes

        session_attr['numberSolutions'] = 0
        session_attr['solutionIndex'] = 1
        session_attr['solution'] = {}
        session_attr['intentname'] = "ProblemIntent"
        session_attr['statement'] = ""
        session_attr['proandcon'] = {}


        speech = ('Hi - I am Lumen, your health coach. My job is to counsel you with problem solving therapy. '
            'The first step is for you to tell me about a problem. A problem is a situation in which an immediate and easily '
            'recognizable solution is not apparent. The problem should focus on the here and now, and currently affecting you. '
            'Also, it should be something you have control over to solve. Think about it for a moment. When you are ready, tell me '
            'about your problem.')
            

        reprompt = 'I am interested in hearing about your problem. Can you tell me a problem you have?'
        
        #if handler_input.dialog_state == "COMPLETED":
        #handler_input.response_builder.speak(speech).ask(reprompt).add_directive(DelegateDirective(updated_intent = 'GoalIntent'))
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response


class ProblemIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("IntentRequest")(handler_input) and
            is_intent_name("ProblemIntent")(handler_input))

    def handle(self, handler_input):
        
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr['intentname'] = "ProblemIntent"
        handler_input.attributes_manager.session_attributes = session_attr
        
        speech = ('Thank you for sharing with me. You have identified a problem and set a goal. Good so far. '
            'Next, I would like you to brainstorm some possible solutions to your problem. This may take a few minutes. Try to '
            "be as creative as possible. Don't limit yourself in any way. When you are ready, tell me your solution, by saying "
            "my solution is. When you're done, no more solutions")

        reprompt = "I am interested in hearing any potential solutions. Say something that begins with my solution is. When you're done, say no more solutions"
        
        handler_input.response_builder.add_directive(DelegateDirective(updated_intent = 'SolutionIntent')).speak(speech).ask(reprompt)
        #handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class SolutionIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("IntentRequest")(handler_input) and
            is_intent_name("SolutionIntent")(handler_input))

    def handle(self, handler_input):
        session_attr = handler_input.attributes_manager.session_attributes
        
        value = handler_input.request_envelope.request.intent.slots['Solution'].value
        session_attr['intentname'] = "SolutionIntent"
        
        session_attr['numberSolutions'] += 1
        session_attr['solution'][session_attr['numberSolutions']] = value
        handler_input.attributes_manager.session_attributes = session_attr
        

        if handler_input.request_envelope.request.dialog_state != DialogState.COMPLETED:
            speech = 'I heard ' + str(value) + '. That is ' + str(session_attr['numberSolutions']) + ' solutions so far. Do you have other solutions? If not, say no more solutions'
            reprompt = " I am interested in hearing any potential solutions. Say something that begins with my solution is. When you're done, say no more solutions"
            handler_input.attributes_manager.session_attributes = session_attr
            handler_input.response_builder.speak(speech).ask(reprompt)
            return handler_input.response_builder.response
            
        else:
            handler_input.attributes_manager.session_attributes = session_attr
            handler_input.response_builder.add_directive(DelegateDirective(updated_intent = "SolutionEndIntent"))
            return handler_input.response_builder.response


class SolutionEndIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("IntentRequest")(handler_input) and
            is_intent_name("SolutionEndIntent")(handler_input))

    def handle(self, handler_input):
        
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr['intentname'] = "SolutionEndIntent"
        handler_input.attributes_manager.session_attributes = session_attr
        
        speech = ("Great effort brainstorming solutions! Now let's move on. For each solution you mentioned, think about all the advantages or pros of that solution. "
            'Also, consider all of the possible disadvantages or "cons" of that solution.')
        reprompt = 'I have heard your solutions. Do you know of any pros or cons?'
        
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr['intentname'] = "SolutionEndIntent"
        handler_input.attributes_manager.session_attributes = session_attr

        #handler_input.response_builder.speak(speech).ask(reprompt)
        handler_input.response_builder.add_directive(DelegateDirective(updated_intent = 'ProsAndConsIntent')).speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class ProsAndConsIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ( is_request_type("IntentRequest")(handler_input) and
            is_intent_name("ProsAndConsIntent")(handler_input))

    def handle(self, handler_input):
        
        session_attr = handler_input.attributes_manager.session_attributes
        value = session_attr['solution'][session_attr['solutionIndex']]
        session_attr['intentname'] = "ProsAndConsIntent"
        handler_input.attributes_manager.session_attributes = session_attr

        i = 1
        session_attr['statement'] = "i"
        handler_input.attributes_manager.session_attributes = session_attr
        
        if session_attr["numberSolutions"] >= i and handler_input.request_envelope.request.dialog_state != DialogState.COMPLETED:
            value = session_attr['solution'][session_attr[i]]
            session_attr['proandcon'][value] = [handler_input.request_envelope.request.intent.slots['Pro'].value]
            session_attr['proandcon'][value].append(handler_input.request_envelope.request.intent.slots['Con'].value)
            handler_input.attributes_manager.session_attributes = session_attr
            i += 1
            speech = 'For your solution' + str(value) + ', say a pro and a con for your solution. Say "a pro is" or "a con is" or "no more pros and cons" to end'
            reprompt = "Any pros and cons for " + str(value) + "?"
            session_attr['statement'] = "if"
            handler_input.attributes_manager.session_attributes = session_attr
            handler_input.response_builder.speak(speech).ask(reprompt)
            return handler_input.response_builder.response
            
        else :
            speech = "You are done with the Pros and Cons. Kindly end this intent by saying 'no more pros and cons'"
            session_attr['statement'] = "else"
            handler_input.attributes_manager.session_attributes = session_attr
            handler_input.response_builder.add_directive(DelegateDirective(updated_intent = "ProsAndConsEndIntent"))
            return handler_input.response_builder.response
            
        

class ProsAndConsEndIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("IntentRequest")(handler_input) and
            is_intent_name("ProsAndConsEndIntent")(handler_input))
    
    def handle(self, handler_input):
        session_attr = handler_input.attributes_manager.session_attributes
        solutionText = ""
        session_attr['intentname'] = "ProsAndConsEndIntent"
        handler_input.attributes_manager.session_attributes = session_attr
        
        
        i = 1
        
        while i <=  int(session_attr["numberSolutions"]) :
            solutionText = solutionText + str(session_attr["solution"][str(i)]) + ","
            i += 1

        speech = 'Thank you for being open about the pros and cons of your solutions. Now I would like you to choose a solution to try for next week. ' + 'Think about which solution is most feasible. Which has the best chance of achieving your goal. ' +'The solutions you have mentioned are ' + str(solutionText) + ' and you can choose one.' + "Start by saying I choose"
        reprompt = "What solution would you like to try?"
        
        handler_input.response_builder.add_directive(DelegateDirective(updated_intent = "SolutionChoiceIntent")).speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class SolutionChoiceIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("IntentRequest")(handler_input) and
            is_intent_name("SolutionChoiceIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr['intentname'] = "SolutionChoiceIntent"
        handler_input.attributes_manager.session_attributes = session_attr

        speech = 'We now go to the final step of making an action plan for your solution. What do you need to do? When will this start? Start by saying "My plan is"'
        reprompt = 'What is your action plan?';
        
        handler_input.response_builder.add_directive(DelegateDirective(updated_intent = "ActionPlanIntent")).speak(speech).ask(reprompt)
        return handler_input.response_builder.response
            
        
class ActionPlanIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("IntentRequest")(handler_input) and
            is_intent_name("ActionPlanIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr['intentname'] = "ActionPlanIntent"
        handler_input.attributes_manager.session_attributes = session_attr
        
        speech = ("Sound's like you have a plan. How confident do you feel on a scale from 1-10, where 1 is not confident at all, and 10 is very confident that "
            ' you will be able to carry out the plan to solve your problem?')
        reprompt = 'On a scale from 1-10, how confident are you that you can carry out your plan?'
        
        handler_input.response_builder.add_directive(DelegateDirective(updated_intent = 'ConfidenceIntent')).speak(speech).ask(reprompt)
        return handler_input.response_builder.response


class ConfidenceIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("IntentRequest")(handler_input) and
            is_intent_name("ConfidenceIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #value = handler_input.request_envelope.request.intent.slots['Confidence'].value;
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr['intentname'] = "ConfidenceIntent"
        handler_input.attributes_manager.session_attributes = session_attr
        
        #speech = 'You said ' + str(value) + '. Thank you for taking the time. I wish you good luck, and look forward to hearing how things go for you next time.'
        speech = "hello world"
        handler_input.response_builder.speak(speech).set_should_end_session(True)
        return handler_input.response_builder.response

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        speech = 'How can I help?'

        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")

        speech = 'Okay then. Hope to speak with you again soon. Goodbye!'
        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.

    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speech = 'Sorry, that is beyond me. Try again?'
        reprompt = 'I am interested in hearing about your problem. Can you tell me a problem you have?'


        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response


class RepeatIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.RepeatIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        session_attr = handler_input.attributes_manager.session_attributes
        
        speech = 'No problem I will repeat the instance for you'
        intent = session_attr['intentname']

        handler_input.response_builder.add_directive(DelegateDirective(updated_intent = intent)).speak(speech)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        logger.info("Session ended reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


# Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.info("In CatchAllExceptionHandler")
        logger.error(exception, exc_info=True)

        speech = "Sorry. I cannot help you with that."
        reprompt = "What can I help you with?"
        handler_input.response_builder.speak(speech).ask(reprompt)

        return handler_input.response_builder.response


# Request and Response loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the alexa requests."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(
            handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the alexa responses."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register intent handlers

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(ProblemIntentHandler())
sb.add_request_handler(SolutionIntentHandler())
sb.add_request_handler(SolutionEndIntentHandler())
sb.add_request_handler(ProsAndConsIntentHandler())
sb.add_request_handler(ProsAndConsEndIntentHandler())
sb.add_request_handler(SolutionChoiceIntentHandler())
sb.add_request_handler(ActionPlanIntentHandler())
sb.add_request_handler(ConfidenceIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(RepeatIntentHandler())

# Register exception handlers
sb.add_exception_handler(CatchAllExceptionHandler())

# TODO: Uncomment the following lines of code for request, response logs.
sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()

