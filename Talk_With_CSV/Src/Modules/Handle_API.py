import streamlit as st
import os

class Deal_With_API:

    @staticmethod
    def load_api_key():
        """
        This function will load the OpenAI API key from the .env file or
        from the user's input and returns it
        """
        if not st.session_state.get("api_key"):
            st.session_state["api_key"] = None

        # you can define your API key in .env directly
        if os.path.exists(".env") and os.environ.get("OPENAI_API_KEY") is not None:
            user_api_key = os.environ["OPENAI_API_KEY"]
            st.sidebar.success("API key loaded from .env", icon="🚀")
        else:
            if st.session_state.api_key is not None:
                user_api_key = st.session_state.api_key
                st.sidebar.success("API key loaded from previous input", icon="🚀")
            else:
                user_api_key = st.sidebar.text_input(
                    label="#### Your OpenAI API key 👇", placeholder="sk-...", type="password"
                )
                if user_api_key:
                    st.session_state.api_key = user_api_key

        return user_api_key

    @staticmethod
    def show_api_key_missing():
        """
        Displays a message if the user has not entered an API key
        """
        st.markdown(
            """
            <div style='text-align: center;'>
                <h1>API Key Requirement ⚠️</h1>
                <p> To use this application, you need to have your own API key from OpenAI. If you don't have an API 
                key, you can get one from the OpenAI website or the link provided below. But if you have your OPENAI 
                API key withyou then enter it in the sidebar to get started.
                </p>
                <h4>Generate your own <a href="https://platform.openai.com/account/api-keys" target="_blank">OpenAI API 
                key</a> to start chatting</h4>
            </div>
            """,
            unsafe_allow_html=True)