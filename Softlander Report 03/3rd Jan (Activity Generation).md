

Code For Activity Generation

```python
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import autogen
# Load environment variables from .env file
load_dotenv()
# Create AssistantAgent and UserProxyAgent
assistant = AssistantAgent("assistant")
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "Maths"})
topic="Simplification in mathematics for a 6-14 year old child"
task1 = f'''
use template.json as presented in the Maths directory above and Make a new json file and fill it with real educational content about {topic}
use this snippet to read the json file
```python
import json
import os
# Check if there's a file named 'template.json' in the maths directory
if os.path.exists('../Maths/template.json'):
    # Open the file
    with open('../Maths/recipe.json', 'r') as file:
        # Load the json content
        data = json.load(file)
```Make use only of the template of the template.json file and fill it with real educational content about {topic}
'''

user_proxy.initiate_chat(assistant, message=task1)
```


  **JSON template for activity generation**


```json
{
  "subject": "",
  "topics": [
    {
      "name": "[Topic Name]",
      "description": "[Engaging story or significance of the topic.]",
      "activity_sets": [
        {
          "difficulty_level": "Beginner",
          "activity": {
            "title": "[Activity Title]",
            "description": "[Story or scenario setting the context of the activity related to the topic]",
            "materials_needed": ["[Material 1]", "[Material 2]"],
            "steps": [
              {"step_number": 1, "description": "[Step 1 details]"},
              {"step_number": 2, "description": "[Step 2 details]"},
              {"step_number": 3, "description": "[Step 3 details]"}
            ],
            "observations": "[Instructions for the teacher]",
            "assessments": [
              {"type": "Self-Assessment", "description": "[Details for self-assessment]"},
              {"type": "Report Writing", "description": "[Details for report writing]"},
              {"type": "Presentation", "description": "[Details for presentation]"},
              {"type": "Poster Making", "description": "[Details for poster making]"}
            ]
          }
        },
        {
          "difficulty_level": "Intermediate",
          "activity": {
            "title": "[Activity Title]",
            "description": "[Story or scenario setting the context of the activity related to the topic]",
            "materials_needed": ["[Material 1]", "[Material 2]"],
            "steps": [
              {"step_number": 1, "description": "[Step 1 details]"},
              {"step_number": 2, "description": "[Step 2 details]"},
              {"step_number": 3, "description": "[Step 3 details]"}
            ],
            "observations": "[Instructions for the teacher]",
            "assessments": [
              {"type": "Self-Assessment", "description": "[Details for self-assessment]"},
              {"type": "Report Writing", "description": "[Details for report writing]"},
              {"type": "Presentation", "description": "[Details for presentation]"},
              {"type": "Poster Making", "description": "[Details for poster making]"}
            ]
          }
        },
        {
          "difficulty_level": "Advanced",
          "activity": {
            "title": "[Activity Title]",
            "description": "[Story or scenario setting the context of the activity related to the topic]",
            "materials_needed": ["[Material 1]", "[Material 2]"],
            "steps": [
              {"step_number": 1, "description": "[Step 1 details]"},
              {"step_number": 2, "description": "[Step 2 details]"},
              {"step_number": 3, "description": "[Step 3 details]"}
            ],
            "observations": "[Instructions for the teacher]",
            "assessments": [
              {"type": "Self-Assessment", "description": "[Details for self-assessment]"},
              {"type": "Report Writing", "description": "[Details for report writing]"},
              {"type": "Presentation", "description": "[Details for presentation]"},
              {"type": "Poster Making", "description": "[Details for poster making]"}
            ]
          }
        }
      ]
    }
  ],
  "output_format": "JSON"
}
  }
```

Eg) For Simplification

```json
{
    "subject": "Mathematics",
    "topics": [
        {
            "name": "Simplification",
            "description": "Simplification makes math easier to understand and solve. Let's learn how with simple activities!",
            "activity_sets": [
                {
                    "difficulty_level": "Beginner",
                    "activity": {
                        "title": "Understanding basic simplification",
                        "description": "In this activity, we will learn how to simplify an expression using basic addition and multiplication.",
                        "materials_needed": [
                            "Pencil",
                            "Paper"
                        ],
                        "steps": [
                            {
                                "step_number": 1,
                                "description": "Write down the expression '2+2+2'."
                            },
                            {
                                "step_number": 2,
                                "description": "Recognize this as the multiplication expression '3*2'."
                            },
                            {
                                "step_number": 3,
                                "description": "Write down and solve the multiplication problem, finding that '3*2' equals 6."
                            }
                        ],
                        "observations": "Observe how the student transforms and solves the expression.",
                        "assessments": [
                            {
                                "type": "Self-Assessment",
                                "description": "Review your steps and ensure you correctly solved the problem."
                            }
                        ]
                    }
                },
                {
                    "difficulty_level": "Intermediate",
                    "activity": {
                        "title": "Solving simplification problems",
                        "description": "Time to solve a bit complicated simplification problems. Remember, multiplication and division first, then addition and subtraction.",
                        "materials_needed": [
                            "Pencil",
                            "Paper"
                        ],
                        "steps": [
                            {
                                "step_number": 1,
                                "description": "Write down the problem '2+3*2'."
                            },
                            {
                                "step_number": 2,
                                "description": "Recognize that you should multiply 3 and 2 before adding 2."
                            },
                            {
                                "step_number": 3,
                                "description": "Solve the problem to find that '2+3*2' equals 8."
                            }
                        ],
                        "observations": "Observe how the student applies the order of operations to simplify the expression.",
                        "assessments": [
                            {
                                "type": "Self-Assessment",
                                "description": "Review your steps and ensure you correctly solved the problem."
                            }
                        ]
                    }
                },
                {
                    "difficulty_level": "Advanced",
                    "activity": {
                        "title": "Mastering simplification",
                        "description": "Ready for a challenge? You'll tackle simplification of a complex expression in this activity.",
                        "materials_needed": [
                            "Pencil",
                            "Paper"
                        ],
                        "steps": [
                            {
                                "step_number": 1,
                                "description": "Write down the problem '(2+3)*4-2^2'."
                            },
                            {
                                "step_number": 2,
                                "description": "Remember the order of operations: brackets first, then exponents (like '2^2'), multiplication and division, and finally addition and subtraction."
                            },
                            {
                                "step_number": 3,
                                "description": "Solve the problem step by step. When you complete all steps, you will find the answer to be 16."
                            }
                        ],
                        "observations": "Observe the order in which the student performs the operations and their understanding of simplification.",
                        "assessments": [
                            {
                                "type": "Self-Assessment",
                                "description": "Did you solve the problem correctly? If not, go through each step again."
                            }
                        ]
                    }
                }
            ]
        }
    ],
    "output_format": "JSON"
}
```