Completed Assessment Generation according to the schema
## fastapi call to generate course

Code 
```python
from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from openai import RateLimitError
app = FastAPI()
# Load environment variables from .env file
load_dotenv()
# Create AssistantAgent and UserProxyAgent
assistant = AssistantAgent("assistant", human_input_mode="NEVER")
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "Course"}, human_input_mode="NEVER")
@app.get("/generate_course")
async def generate_course(topic: str = Query(..., description="The topic for which the course should be generated")):
    try:
        user_proxy.initiate_chat(
            assistant,
            message=f""" Generate a course for the topic {topic} and keep in mind it is only for the age group 6-14 year old children, generate it in a suitable json format and save it in this directory itself. Add at least 10 topics along with their subtopics so that there is enough for the child to learn. Structure the Json Properly and name the json {topic}.json. If you are making any additional python files call it only generator.py and dont make any additional python files and keep the json parameters standard keep ONLY Course, Topics and Subtopics and make proper json format by looking at {{
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
        return {"message": f"Course generation initiated for the topic: {topic}. Note: OpenAI API rate limit reached. Please try again later."}
    return {"message": f"Course generation initiated for the topic: {topic}"}
```

#### This code accepts a subject name in the API request and generates the topics according to the provided schema

![[Pasted image 20240108121608.png]]

Generates a Learning Path for the provided subject name

```json
{
    "Course": "Mathematics",
    "Path": [
        {
            "Numbers": {
                "Topics": [
                    "Whole Numbers",
                    "Decimal Numbers",
                    "Fractions"
                ]
            }
        },
        {
            "Geometry": {
                "Topics": [
                    "Shapes",
                    "Lines",
                    "Angles"
                ]
            }
        },
        {
            "Measurement": {
                "Topics": [
                    "Length",
                    "Weight",
                    "Volume"
                ]
            }
        },
        {
            "Data": {
                "Topics": [
                    "Representing Data",
                    "Reading Graphs",
                    "Probability"
                ]
            }
        },
        {
            "Algebra": {
                "Topics": [
                    "Introduction to Algebra",
                    "Basic Equations",
                    "Word Problems"
                ]
            }
        },
        {
            "Fractions": {
                "Topics": [
                    "Comparing fractions",
                    "Adding and Subtracting Fractions",
                    "Multiplying and Dividing Fractions"
                ]
            }
        },
        {
            "Decimals": {
                "Topics": [
                    "Comparing Decimals",
                    "Rounding Decimals",
                    "Math with Decimals"
                ]
            }
        },
        {
            "Percentages": {
                "Topics": [
                    "Understanding percentages",
                    "Comparing and Ordering Percentages",
                    "Ratio and Proportion"
                ]
            }
        },
        {
            "Patterns and Sequences": {
                "Topics": [
                    "Shapes and Patterns",
                    "Number Patterns",
                    "Algebraic Expressions"
                ]
            }
        },
        {
            "Mathematical Logic": {
                "Topics": [
                    "Inductive Reasoning",
                    "Deductive Reasoning",
                    "Fallacies and Paradoxes"
                ]
            }
        }
    ]
}
```

