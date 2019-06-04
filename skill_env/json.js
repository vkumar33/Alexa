{
    "interactionModel": {
        "languageModel": {
            "invocationName": "lumen coach",
            "intents": [
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.NavigateHomeIntent",
                    "samples": []
                },
                {
                    "name": "ProblemIntent",
                    "slots": [
                        {
                            "name": "Problem",
                            "type": "AMAZON.SearchQuery",
                            "samples": [
                                "{Problem}",
                                "I am concerned about {Problem}",
                                "I have a problem with {Problem}",
                                "My problem is {Problem}"
                            ]
                        },
                        {
                            "name": "Goal",
                            "type": "AMAZON.SearchQuery",
                            "samples": [
                                "My goal is {Goal}",
                                "{Goal}",
                                "I want to {Goal}",
                                "I wish to {Goal}",
                                "I hope to {Goal}",
                                "My goal is to {Goal}"
                            ]
                        }
                    ],
                    "samples": [
                        "{Problem} is trouble for me",
                        "i am worried about {Problem}",
                        "{Problem} is my problem",
                        "my problem is {Problem}"
                    ]
                },
                {
                    "name": "SolutionIntent",
                    "slots": [
                        {
                            "name": "Solution",
                            "type": "AMAZON.SearchQuery",
                            "samples": [
                                "one solution is {Solution}",
                                "another possibility is {Solution}",
                                "another thing I could do is {Solution}",
                                "another solution is {Solution}",
                                "{Solution}",
                                "my solution is {Solution}"
                            ]
                        }
                    ],
                    "samples": [
                        "{Solution} is my solution",
                        "my solution is {Solution}"
                    ]
                },
                {
                    "name": "ProsAndConsIntent",
                    "slots": [
                        {
                            "name": "Pro",
                            "type": "AMAZON.SearchQuery"
                        },
                        {
                            "name": "Con",
                            "type": "AMAZON.SearchQuery",
                            "samples": [
                                "An disadvantage is {Con}",
                                "A Con is {Con}",
                                "One disadvantage might be {Con}",
                                "One bad thing is {Con}",
                                "Con is {Con}",
                                "Bad is {Con}"
                            ]
                        }
                    ],
                    "samples": [
                        "Bad is {Con}",
                        "Good is {Pro}",
                        "Con is {Con}",
                        "Pro is {Pro}",
                        "One bad thing is {Con}",
                        "One good thing is {Pro}",
                        "A con is {Con}",
                        "One disadvantage might be {Con}",
                        "A disadvantage is {Con}",
                        "One advantage might be {Pro}",
                        "A pro is {Pro}",
                        "An advantage is {Pro}"
                    ]
                },
                {
                    "name": "SolutionEndIntent",
                    "slots": [],
                    "samples": [
                        "i am done with solutions",
                        "i have no more solutions",
                        "no more solutions"
                    ]
                },
                {
                    "name": "ProsAndConsEndIntent",
                    "slots": [],
                    "samples": [
                        "i have no more pros and cons",
                        "no more pros and cons",
                        "i am done with pros and cons"
                    ]
                },
                {
                    "name": "SolutionChoiceIntent",
                    "slots": [
                        {
                            "name": "SolutionChoice",
                            "type": "AMAZON.SearchQuery",
                            "samples": [
                                "{SolutionChoice} is my choice",
                                "I want to {SolutionChoice}",
                                "I choose {SolutionChoice}"
                            ]
                        }
                    ],
                    "samples": [
                        "{SolutionChoice} is my choice",
                        "i choose {SolutionChoice}"
                    ]
                },
                {
                    "name": "ActionPlanIntent",
                    "slots": [
                        {
                            "name": "ActionPlan",
                            "type": "AMAZON.SearchQuery",
                            "samples": [
                                "I am going to {ActionPlan}",
                                "I plan to {ActionPlan}",
                                "I need to {ActionPlan}"
                            ]
                        }
                    ],
                    "samples": [
                        "I need to {ActionPlan}",
                        "I am going to {ActionPlan}",
                        "I will {ActionPlan}",
                        "I plan to {ActionPlan}"
                    ]
                },
                {
                    "name": "ActionPlanEndIntent",
                    "slots": [],
                    "samples": [
                        "i have no more actions to say",
                        "i have no more actions to add",
                        "my action plan is done",
                        "no more actions"
                    ]
                },
                {
                    "name": "ConfidenceIntent",
                    "slots": [
                        {
                            "name": "Confidence",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "{Confidence}",
                        "I am a {Confidence} out of ten"
                    ]
                },
                {
                    "name": "AMAZON.FallbackIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.RepeatIntent",
                    "samples": []
                }
            ],
            "types": []
        },
        "dialog": {
            "intents": [
                {
                    "name": "ProblemIntent",
                    "confirmationRequired": true,
                    "prompts": {
                        "confirmation": "Confirm.Intent.960613033858"
                    },
                    "slots": [
                        {
                            "name": "Problem",
                            "type": "AMAZON.SearchQuery",
                            "confirmationRequired": true,
                            "elicitationRequired": true,
                            "prompts": {
                                "confirmation": "Confirm.Slot.18288425427.207857648845",
                                "elicitation": "Elicit.Slot.18288425427.207857648845"
                            }
                        },
                        {
                            "name": "Goal",
                            "type": "AMAZON.SearchQuery",
                            "confirmationRequired": true,
                            "elicitationRequired": true,
                            "prompts": {
                                "confirmation": "Confirm.Slot.1311459165236.651038751576",
                                "elicitation": "Elicit.Slot.1311459165236.651038751576"
                            }
                        }
                    ]
                },
                {
                    "name": "SolutionIntent",
                    "confirmationRequired": false,
                    "prompts": {},
                    "slots": [
                        {
                            "name": "Solution",
                            "type": "AMAZON.SearchQuery",
                            "confirmationRequired": true,
                            "elicitationRequired": true,
                            "prompts": {
                                "confirmation": "Confirm.Slot.812942704779.27889244345",
                                "elicitation": "Elicit.Slot.334262902940.508683137030"
                            }
                        }
                    ]
                },
                {
                    "name": "SolutionChoiceIntent",
                    "confirmationRequired": true,
                    "prompts": {
                        "confirmation": "Confirm.Intent.974585561998"
                    },
                    "slots": [
                        {
                            "name": "SolutionChoice",
                            "type": "AMAZON.SearchQuery",
                            "confirmationRequired": false,
                            "elicitationRequired": true,
                            "prompts": {
                                "elicitation": "Elicit.Slot.571859132695.902606340299"
                            }
                        }
                    ]
                },
                {
                    "name": "ActionPlanIntent",
                    "confirmationRequired": false,
                    "prompts": {},
                    "slots": [
                        {
                            "name": "ActionPlan",
                            "type": "AMAZON.SearchQuery",
                            "confirmationRequired": false,
                            "elicitationRequired": true,
                            "prompts": {
                                "elicitation": "Elicit.Slot.24341360755.191033678369"
                            }
                        }
                    ]
                },
                {
                    "name": "ConfidenceIntent",
                    "confirmationRequired": false,
                    "prompts": {},
                    "slots": [
                        {
                            "name": "Confidence",
                            "type": "AMAZON.NUMBER",
                            "confirmationRequired": false,
                            "elicitationRequired": false,
                            "prompts": {}
                        }
                    ]
                },
                {
                    "name": "SolutionEndIntent",
                    "confirmationRequired": true,
                    "prompts": {
                        "confirmation": "Confirm.Intent.788742071724"
                    },
                    "slots": []
                },
                {
                    "name": "ProsAndConsIntent",
                    "confirmationRequired": false,
                    "prompts": {},
                    "slots": [
                        {
                            "name": "Pro",
                            "type": "AMAZON.SearchQuery",
                            "confirmationRequired": false,
                            "elicitationRequired": false,
                            "prompts": {}
                        },
                        {
                            "name": "Con",
                            "type": "AMAZON.SearchQuery",
                            "confirmationRequired": true,
                            "elicitationRequired": true,
                            "prompts": {
                                "confirmation": "Confirm.Slot.690646501250.780469113880",
                                "elicitation": "Elicit.Slot.690646501250.780469113880"
                            }
                        }
                    ]
                },
                {
                    "name": "ProsAndConsEndIntent",
                    "confirmationRequired": true,
                    "prompts": {
                        "confirmation": "Confirm.Intent.201078496191"
                    },
                    "slots": []
                }
            ],
            "delegationStrategy": "ALWAYS"
        },
        "prompts": [
            {
                "id": "Confirm.Intent.960613033858",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "You said {Problem} with a goal of {Goal} . Do I have this right so far?"
                    },
                    {
                        "type": "PlainText",
                        "value": "It sounds like {Problem} is a problem for you, and {Goal} is your goal. Is that correct so far?"
                    }
                ]
            },
            {
                "id": "Elicit.Slot.18288425427.207857648845",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "What problem can you tell me about?"
                    },
                    {
                        "type": "PlainText",
                        "value": "Can you briefly describe a problem for me?"
                    },
                    {
                        "type": "PlainText",
                        "value": "Please tell me about a problem"
                    }
                ]
            },
            {
                "id": "Confirm.Slot.18288425427.207857648845",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "I heard you say {Problem} - do I have this correct?"
                    },
                    {
                        "type": "PlainText",
                        "value": "You said {Problem} - is that right?"
                    }
                ]
            },
            {
                "id": "Elicit.Slot.1311459165236.651038751576",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "I would like to know next what your goal is. What goal would you like to set. Say something that begins with my goal is"
                    },
                    {
                        "type": "PlainText",
                        "value": "Please tell me your goal. What do you hope to achieve by addressing this problem. Say something that begins with my goal is"
                    },
                    {
                        "type": "PlainText",
                        "value": "The next step is to describe a goal. What do you hope to achieve by solving this problem. Say something that begins with my goal is"
                    }
                ]
            },
            {
                "id": "Confirm.Slot.1311459165236.651038751576",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "You said {Goal} . Your goal should be SMART - specific, measurable, actionable, realistic, and time-bound. Are you okay with this goal?"
                    },
                    {
                        "type": "PlainText",
                        "value": "You said {Goal} . Your goal should be SMART - specific, measurable, actionable, realistic, and time-bound. Does this goal work for you?"
                    }
                ]
            },
            {
                "id": "Elicit.Slot.334262902940.508683137030",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "Can you suggest a possible solution?"
                    },
                    {
                        "type": "PlainText",
                        "value": "Please provide a solution. Be creative. Don't limit yourself."
                    }
                ]
            },
            {
                "id": "Confirm.Intent.974585561998",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "are you sure you want to go with {SolutionChoice} ?"
                    },
                    {
                        "type": "PlainText",
                        "value": "is {SolutionChoice} work best for you?"
                    }
                ]
            },
            {
                "id": "Elicit.Slot.571859132695.902606340299",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "Tell me what solution do you want to choose. Say I choose and your solution."
                    },
                    {
                        "type": "PlainText",
                        "value": "Which solution do you choose?"
                    }
                ]
            },
            {
                "id": "Elicit.Slot.24341360755.1446632544696",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "What is the date when this will begin?"
                    },
                    {
                        "type": "PlainText",
                        "value": "Tell me the date of when this will start?"
                    }
                ]
            },
            {
                "id": "Elicit.Slot.24341360755.191033678369",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "What else do you need to do for your solution?"
                    },
                    {
                        "type": "PlainText",
                        "value": "What is your action plan?"
                    }
                ]
            },
            {
                "id": "Confirm.Slot.812942704779.27889244345",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "You have suggested these solutions - {Solution} . When you're done, say no more solutions or i am done with solutions"
                    }
                ]
            },
            {
                "id": "Confirm.Intent.788742071724",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "Are you done with solutions"
                    }
                ]
            },
            {
                "id": "Elicit.Slot.690646501250.780469113880",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "Can you please suggest another Con"
                    }
                ]
            },
            {
                "id": "Confirm.Slot.690646501250.780469113880",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "You have suggested these Cons - {Con} . When you're done with all Pros and Cons, say no more pros and cons or I am done with Pros and cons"
                    }
                ]
            },
            {
                "id": "Confirm.Intent.201078496191",
                "variations": [
                    {
                        "type": "PlainText",
                        "value": "Are you done with Pros and Cons"
                    }
                ]
            }
        ]
    }
}