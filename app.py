import streamlit as st

st.set_page_config(page_title="LLM App Constructor", page_icon="🤖", layout="centered")

st.title("🤖 Конструктор LLM-приложений")
st.markdown("""
Создайте собственное приложение на базе ИИ без программирования!\n\n
1. Опишите цель приложения
2. Загрузите свои данные
3. Выберите модель ИИ и настройте промпт
4. Получите готовое приложение и поделитесь с коллегами
""")

if st.button("Создать приложение"):
    st.session_state["step"] = 1
    st.experimental_rerun()

if st.session_state.get("step") == 1:
    st.header("Шаг 1: Опишите цель вашего приложения")
    app_goal = st.text_area("Опишите, для чего вы хотите создать приложение", key="app_goal")
    if st.button("Далее", key="to_step_2"):
        st.session_state["app_goal"] = app_goal
        st.session_state["step"] = 2
        st.experimental_rerun() 