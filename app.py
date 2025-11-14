from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

# OpenAI LLMの初期化
llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# テンプレートの定義
template1 = """
あなたは、スポーツのルールに詳しいAIです。ユーザーが入力したスポーツのルールを100文字程度で説明してください。
スポーツ名：{sport_name}
説明：
"""

template2 = """
あなたは、果物の調理方法に詳しいAIです。ユーザーが入力した果物の調理方法を100文字程度で提案してください。
果物名：{fruit_name}
提案：
"""

st.title("スポーツのルールと果物の調理に詳しいAI")

st.write("##### 動作モード1: スポーツのルールを教えてくれるAI")
st.write("入力フォームにルールを知りたいスポーツ名を入力して「実行」ボタンを押してください。")
st.write("##### 動作モード2: 果物の調理方法に詳しいAI")
st.write("調理したい果物名を入力して「実行」ボタンを押してください。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["スポーツのルールを教えてくれるAI", "果物の調理方法に詳しいAI"]
)

st.divider()

if selected_item == "スポーツのルールを教えてくれるAI":
    sport_name = st.text_input(label="スポーツ名を入力してください。")
else:
    fruit_name = st.text_input(label="果物名を入力してください。")

if st.button("実行"):
    st.divider()
    
    if selected_item == "スポーツのルールを教えてくれるAI":
        if sport_name:
            st.write(f"スポーツ名: **{sport_name}**")
            
            prompt = PromptTemplate(
                input_variables=["sport_name"],
                template=template1,
            )
            message = prompt.format(sport_name=sport_name)
            
            # LLMで回答を生成
            with st.spinner("AIが回答を生成中..."):
                response = llm.invoke(message)
                st.write("### 回答:")
                st.write(response.content)
        else:
            st.error("スポーツ名を入力してから「実行」ボタンを押してください。")
    
    else:
        if fruit_name:
            st.write(f"果物名: **{fruit_name}**")
            
            prompt = PromptTemplate(
                input_variables=["fruit_name"],
                template=template2,
            )
            message = prompt.format(fruit_name=fruit_name)
            
            # LLMで回答を生成
            with st.spinner("AIが回答を生成中..."):
                response = llm.invoke(message)
                st.write("### 回答:")
                st.write(response.content)
        else:
            st.error("果物名を入力してから「実行」ボタンを押してください。")