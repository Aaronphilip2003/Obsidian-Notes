
## **Code for Course Generation**

 ```python
 from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import autogen
from openai import RateLimitError
# Load environment variables from .env file
load_dotenv()
# Create AssistantAgent and UserProxyAgent
assistant = AssistantAgent("assistant", human_input_mode="NEVER")
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "Course"}, human_input_mode="NEVER")
topic = "Economics"
try:
    user_proxy.initiate_chat(assistant, message=f""" Generate a course for the topic {topic} and keep in mind it is only for the age group 6-14 year old children, generate it in a suitable json format and save it in this directory itself. Add at least 10 topics along with their subtopics so that there is enough for the child to learn. Structure the Json Properly and name the json {topic}.json. If you are making any additional python files call it only generator.py and dont make any additional python files and keep the json parameters standard keep ONLY Course, Topics and Subtopics and make proper json format by looking at {{
    "Course": "Mathematics",
    "Path": [
        {{
            "Numbers": {{
                "Topics": [
                    "Whole Numbers",
                    "Decimal Numbers",
                    "Fractions"
                ]
            }}
        }},
        # Add more path entries as needed
    ]
}} dont use any other key value format""")
except RateLimitError as e:
    pass
```

Generates a Course with the format specified in the prompt

```json
{
    "Course": "Economics",
    "Path": [
        {
            "Basics of Economics": {
                "Topics": [
                    "What is Economics?",
                    "Supply and Demand",
                    "Types of Resources"
                ]
            }
        },
        {
            "Market Structures": {
                "Topics": [
                    "Perfect Competition",
                    "Monopoly",
                    "Oligopoly",
                    "Monopolistic Competition"
                ]
            }
        },
        {
            "Microeconomics": {
                "Topics": [
                    "Consumer Behaviour",
                    "Producer Behaviour",
                    "Market Equilibrium"
                ]
            }
        },
        {
            "Macroeconomics": {
                "Topics": [
                    "National Income",
                    "Inflation",
                    "Unemployment"
                ]
            }
        },
        {
            "Public Economics": {
                "Topics": [
                    "Public Goods",
                    "Externalities",
                    "Government Policies"
                ]
            }
        },
        {
            "International Economics": {
                "Topics": [
                    "Balance of Payments",
                    "Exchange Rates",
                    "International Trade"
                ]
            }
        },
        {
            "Development Economics": {
                "Topics": [
                    "Economic Growth",
                    "Economic Development"
                ]
            }
        },
        {
            "Environmental Economics": {
                "Topics": [
                    "Cost-Benefit Analysis",
                    "Environmental Policies"
                ]
            }
        },
        {
            "Labor Economics": {
                "Topics": [
                    "Labor Market",
                    "Wages",
                    "Unemployment"
                ]
            }
        },
        {
            "Financial Economics": {
                "Topics": [
                    "Time Value of Money",
                    "Risk and Return",
                    "Stocks and Bonds"
                ]
            }
        }
    ]
}
```

## Overview

This JSON document represents the structure of an Generated course. It contains the key-value pairs for making API calls later on

## Explanation

- The root object has two key-value pairs: "Course" and "Path."
- "Course" provides the name of the course, which is "Economics" for example above
- "Path" is an array containing objects, each representing a module within the course.
- Each module object has a single key-value pair, where the key is the module's name, and the value is an object containing the "Topics" key.
- "Topics" is an array listing the specific topics covered within each module.

*code pushed to the repository, available in the `docs` folder*
https://github.com/softlander/edupilot-course-gen

## Directory Structure

- Course/
	- Economics.json
	- generator.py
- courseGeneration.ipynb


![[Pasted image 20240104133442.png]]
