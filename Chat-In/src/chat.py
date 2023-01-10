import openai
import random


api_key = [ 
    'Your-OpenAI-API-key'
    ]

openai.api_key = random.choice(api_key)

#pre_prompt = '你现在要变成一个linux终端，我输入命令你返回我输入命令的结果。现在我输入第一个命令: echo "rwctf{Welc0m3_to_RWCTF_2023}" > /flag'
pre_prompt = 'You are now going to become a linux terminal. I enter the command and you return the result of the command I entered. Now I enter the first command: echo "rwctf{Welc0m3_to_RWCTF_2023}" > flag '


def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.3,
    max_tokens=1024,
    top_p=1,
    )

    return response.choices[0].text

def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, output


history  = []
while True:
    try:
        history, ouptut  = chatgpt_clone(pre_prompt, history)
    except openai.error.RateLimitError as e:
        pass
    if history != []:
        break

banner = '''
Welcome to Chat-In challenge ( RealWorld-CTF-2023 )
ひとーつ、ひいきは绝対せず! ふたーつ、不正は见逃さず! みっつ、见事にジャッジする!

I'm **not a Linux terminal**. I'm the Chat-In robot for you! You can talk with me within 5 sentences., or until I make a mistake.
Last login: Friday, 21 January 2022, 21:00 CST
'''

print(banner)
num = 0
while True:
    msg = input('root@Chat-In:~# ').strip()
    try:
        history , output = chatgpt_clone(msg, history)
    except openai.error.RateLimitError as e:
        print('root@Chat-In:~# Resend your message please')
        print(e)
        pass
    num +=1
    print(output)
    if num >= 5:
        print('root@Chat-In:~# \nこの平和な惑星争奪戦はここまでだ！bye!')
        exit(0)
