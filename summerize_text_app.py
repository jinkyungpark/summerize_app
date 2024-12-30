import streamlit as st
from openai import OpenAI

# 기능 구현
def askGpt(prompt, apikey):
    """
    GPT-4o 에게 질문한 후 답변 리턴
    """
    client = OpenAI(api_key=apikey)
    message_prompt = [{"role": "system", "content": prompt}]
    response = client.chat.completions.create(model="gpt-4o", messages=message_prompt)
    gpt_response = response.choices[0].message.content
    return gpt_response


# 메인
def main():
    st.set_page_config(page_title="요약 프로그램")

    # session state 초기화
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    with st.sidebar:
        # open ai api키 입력받기
        open_apikey = st.text_input(
            label="OPENAI API 키",
            placeholder="Enter Your API Key",
            value="",
            type="password",
        )
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
        st.markdown("---")

    st.header("📃요약 프로그램")
    st.markdown("---")

    text = st.text_area("요약 할 글을 입력하세요")
    if st.button("요약"):
        prompt = f"""
        **Instructions** :
    - You are an expert assistant that summarizes text into **Korean language**.
    - Your task is to summarize the **text** sentences in **Korean language**.
    - Your summaries should include the following :
        - Omit duplicate content, but increase the summary weight of duplicate content.
        - Summarize by emphasizing concepts and arguments rather than case evidence.
        - Summarize in 3 lines.
        - Use the format of a bullet point.
    -text : {text}
    """
        st.info(askGpt(prompt, st.session_state["OPENAI_API"]))


if __name__ == "__main__":
    main()
