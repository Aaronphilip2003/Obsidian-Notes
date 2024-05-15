
### No human feedback required while generation  

**Tested Platform : Microsoft Autogen

```python
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
load_dotenv()


assistant = AssistantAgent("assistant",human_input_mode="NEVER")

user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "course_qna"},human_input_mode="NEVER")
user_proxy.initiate_chat(assistant, message="I want you generate a simple course for probability and statistics to explain to a 6 to 14 year old child, save the generated qna in a json file make atleast 20 questions per topic, also We want to generate content, qna, hints for teacher and qna Also the translation into a number of languages. Do all of this for that topic")
```

Results 

```json
{"probability": {"content": "Probability is the branch of mathematics concerning numerical descriptions of how likely an event is to occur, or how likely it is that a proposition is true.", "questions": ["What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation.", "What is probability?", "Give an example of a probability calculation."], "answers": ["Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5.", "Probability is the numerical description of how likely an event is to occur or how likely it is that a proposition is true.", "If a coin is flipped, the probability of it landing on heads is 0.5."], "hints_for_teachers": ["Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins.", "Use real world examples to explain probability.", "Try using different methods of explaining probability, such as using dice or coins."]}, "statistics": {"content": "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "questions": ["What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?", "What is statistics?", "Why is statistics important?"], "answers": ["Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data.", "Statistics is a branch of mathematics dealing with data collection, analysis, interpretation, presentation, and organization.", "Statistics is important because it helps us make decisions based on data."], "hints_for_teachers": ["Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding.", "Use real-life examples to explain statistics.", "Try to use visual representations of data to aid understanding."]}}
```

Working Format

![[Pasted image 20240102140531.png]]


## Tasks to do

- [x] Better the prompts
- [ ] Generate mcqs and qna separately
- [ ] Concluded that json are the best alternatives for  generating activities
- [ ] course generation autopilot 