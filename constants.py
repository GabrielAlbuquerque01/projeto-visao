PATH_JSON_QUESTIONS = r'jsons\v2_OpenEnded_mscoco_val2014_questions.json'
PATH_JSON_ANNOTATIONS = r'jsons\v2_mscoco_val2014_annotations.json'
OPENAI_KEY = ''
PROMPT_CONSTRUCAO_TEXTO = '''Given the image, the question and the answer, your task is to:
1. Generate an accurate 〈Description 1〉 which can be used for
answering the question correctly without using the image.
2. Generate a wrong description 〈Description 2〉 which can be
used for answering the question with a completely wrong answer
〈answer 2〉 without using the image.
3. Make sure both descriptions are sound and concise.
4. The wrong description’s sentence structure should be similar
to the correct description.
Here are the questions and answers:
Question: {question}
Answer: {answer}
Please output the two statements in this format:
Description 1: 〈Description 1〉
Description 2: 〈Description 2〉
Answer 2: 〈answer 2〉
'''

PROMPT_SANITY_CHECK = '''Answer the following question given the text:
Text: {text}
Question: {question}

Respond only with the final answer, without explanation or full sentences.'''


PROMPT_MIX_RESPONSE = '''
Here are some additional information which are text descriptions
based on the image to assist you for answering the later question.
Note, the information could be irrelevant, missing some information
or inaccurate, please use it with caution:
{text_information}
---------------------------
{question}

Respond only with the final answer, without explanation or full sentences.'''