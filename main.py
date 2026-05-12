import streamlit as st
from utils import generate

st.title("🎦1分钟学习街霸6<视频脚本生成>")

with st.sidebar:
    API_key=st.text_input("请输入API密钥",type="password")
    st.markdown("[SF6官方地址](https://www.streetfighter.com/6/zh-hant)")

character = st.text_input("请输入查询人物")
style = st.text_input("请输入操作模式")

submit= st.button("生成攻略")

if submit and not API_key:
    st.info("请输入你的密钥（中文）")
if submit and not style:
    st.info("请输入你的操作模式（中文）")
    st.stop()
if submit and not character:
    st.info("请输入你的人物（中文）")
    st.stop()
if submit:
    with st.spinner(("AI正在胡编中:")):
        response  = generate(API_key,character,style)
    st.success("success")
    st.write(response)