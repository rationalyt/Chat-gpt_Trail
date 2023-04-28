import openai
openai.api_key = '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'
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
#print(openai.Model.list())
openai.organization = "org-aptFU94MxuHPTRC94rmCXnyM"
while True:
    message = input("Enter Wikipedia Link : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
