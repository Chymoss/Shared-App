from langchain.chat_models import init_chat_model
import os
# deepseek用法
from langchain_deepseek import ChatDeepSeek
#model = ChatDeepSeek(model="deepseek-chat", api_key=os.environ.get('DEEPSEEK_API_KEY'))
from langchain_core.messages import HumanMessage


def generate(API_key, character,style):
    model = ChatDeepSeek(model="deepseek-chat", api_key=API_key)
    prompt = f"""
    请围绕街霸6游戏人物“{character}”
    生成一段150词以内的视频脚本，展示{style}操作模式下该角色基本连段和实战思路。

    要求：
    1. 语言自然流畅
    2. 适合短视频口播
    3. 有吸引力
    4. 控制在150词以内
    """

    response = model.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content

#print(generate("玩街霸6游戏"))