import openai

openai.api_key = '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'
openai.organization = 'org-mR5oJ7gGXFJpCsJrKjOCirkC'

chathistory = []

def chatgpt_response(prompt):
    chathistory.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k-0613",
    messages = chathistory,
    temperature=1,
    max_tokens=100
    )
    response_dict = response.get('choices')
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["message"]["content"]
        chathistory.append({"role": 
                            response.choices[0].message.role, "content": response.choices[0].message.content})
        print(chathistory)
    return prompt_response