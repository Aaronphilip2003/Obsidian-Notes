## **Code for Assessment Generation**

```python
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
# Load environment variables from .env file
load_dotenv()
# Create AssistantAgent and UserProxyAgent
assistant = AssistantAgent("assistant", human_input_mode="NEVER")
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "Assessments"}, human_input_mode="NEVER")
topic = "Logic"
# Initiate chat between the two agents to solve the task
user_proxy.initiate_chat(assistant, message=f"""
Create assessments for the topic {topic} and generate 10 assessments in total including all the formats keeping the age group 6-14 years in mind following this template
{{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "definitions": {{
        "mcq": {{
            "type": "object",
            "properties": {{
                "type": {{
                    "const": "mcq"
                }},
                "question": {{
                    "type": "string"
                }},
                "options": {{
                    "type": "object",
                    "properties": {{
                        "a": {{
                            "type": "string"
                        }},
                        "b": {{
                            "type": "string"
                        }},
                        "c": {{
                            "type": "string"
                        }},
                        "d": {{
                            "type": "string"
                        }}
                    }},
                    "required": [
                        "a",
                        "b",
                        "c",
                        "d"
                    ]
                }},
                "answer": {{
                    "type": "string"
                }}
            }},
            "required": [
                "type",
                "question",
                "options",
                "answer"
            ]
        }},
        "fib": {{
            "type": "object",
            "properties": {{
                "type": {{
                    "const": "fib"
                }},
                "question": {{
                    "type": "string"
                }},
                "answer": {{
                    "type": "string"
                }}
            }},
            "required": [
                "type",
                "question",
                "answer"
            ]
        }},
        "sa": {{
            "type": "object",
            "properties": {{
                "type": {{
                    "const": "sa"
                }},
                "question": {{
                    "type": "string"
                }},
                "answer": {{
                    "type": "string"
                }}
            }},
            "required": [
                "type",
                "question",
                "answer"
            ]
        }},
        "tnf": {{
            "type": "object",
            "properties": {{
                "type": {{
                    "const": "tnf"
                }},
                "question": {{
                    "type": "string"
                }},
                "answer": {{
                    "type": "string"
                }}
            }},
            "required": [
                "type",
                "question",
                "answer"
            ]
        }}
    }},
    "type": "object",
    "properties": {{
        "questions": {{
            "type": "array",
            "items": {{
                "oneOf": [
                    {{
                        "$ref": "#/definitions/mcq"
                    }},
                    {{
                        "$ref": "#/definitions/fib"
                    }},
                    {{
                        "$ref": "#/definitions/sa"
                    }},
                    {{
                        "$ref": "#/definitions/tnf"
                    }}
                ]
            }}
        }}
    }},
    "required": [
        "questions"
    ]
}}
and then save it as {topic}_assessment.json, generate a total of 10 assessments including mcq, fib, sa, tnf complying with the given format and save them in the same json as told above.
Use the format shown in the template above and create 2 questions of each type so that we have 10 questions in total.
stick to the template provided above and also copy the boilerplate as it is and fill the rest accordingly with content
""")
```



## Overview

This JSON document represents the structure of an Generated Assessments. It contains the key-value pairs for making API calls later on

1. **Schema Definition:**
    
    - `$schema`: Specifies the URI of the JSON Schema version in use (`http://json-schema.org/draft-07/schema#`).
2. **Definitions:**
    
    - This section defines custom schema types used in the main structure.
    - Four custom types are defined: `mcq`, `fib` (fill in the blank), `sa` (short answer), and `tnf` (true or false).
3. **Custom Types (`mcq`, `fib`, `sa`, `tnf`):**
    
    - Each type has specific properties and constraints.
        - `type`: Specifies the type of question.
        - `question`: Holds the question text.
        - `options` (for `mcq` only): Provides multiple-choice options.
        - `answer`: Contains the correct answer.
4. **Main Structure:**
    
    - `type`: Specifies that the main structure is an object.
    - `properties`: Describes the properties of the main object.
        - `questions`: An array of questions.
            - `type`: Specifies that it is an array.
            - `items`: Describes the items within the array.
                - `oneOf`: Specifies that items in the array must conform to one of the defined custom types (`mcq`, `fib`, `sa`, `tnf`).
5. **Required Fields:**
    
    - `questions`: Mandates that the `questions` array must be present in the main structure.
6. **Questions Data Array:**
    
    - This array contains 10 questions, each represented as an object.
        - Each question object must adhere to one of the custom types defined earlier (`mcq`, `fib`, `sa`, `tnf`).
        - Example `mcq` questions have a `question` text, `options` for multiple choices, and the correct `answer`.
        - Example `fib` questions have a `question` text and the correct `answer`.
        - Example `sa` questions have a `question` text and the correct `answer`.
        - Example `tnf` questions have a `question` text and the correct `answer`.
7. **Example Questions:**
    
    - Demonstrates how to use the defined custom types for various question formats.
    - Covers multiple-choice (`mcq`), fill in the blank (`fib`), short answer (`sa`), and true/false (`tnf`) question types.


*code pushed to the repository, available in the `docs` folder called assessments.ipynb* 
https://github.com/softlander/edupilot-course-gen


![[Pasted image 20240105121352.png]]
