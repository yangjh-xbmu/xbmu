define s = Character('希尔维亚', color="#c8ffc8")
define m = Character('我', color="#c8c8ff")

init python:

    import requests
    import json
    import deepseekkey


    def call_deepseek_api(prompt):
        url = "https://api.deepseek.com/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {deepseekkey.key}"
        }
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return {"error": f"API call failed with status code {response.status_code}"}




label start:

    # python:
    #     content = call_deepseek_api('hi')

    play music "audio/backroad.ogg" 

    scene bg classroom
    with fade

        # 获取用户输入
    $ user_input = renpy.input("问点什么吧：")

    # 调用API生成回答
    $ content = call_deepseek_api(user_input)

    s "hi！[content]"

    m "挺好的……"

    stop music

    "我当然不会承认，上课的时候内容只是左耳进右耳出。"

    show stu at right
    with dissolve

    s "你现在要回家了吗？要不要跟我一起走？"

    m "当然！"

    "你今天穿的好好看！"

menu:

    "是一种视频游戏。":
        jump game

    "是一种互动小说。":
        jump book

label game:

    m "是一种可以在电脑和主机上玩的视频游戏。"

    jump marry

label book:

    m "就像一种可以在电脑和主机上阅读的互动式图书。"

    jump marry

label marry:

    "那么，我们已经成为视觉小说创作二人组了。"

    return
