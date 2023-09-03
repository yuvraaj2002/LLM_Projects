import os
import importlib
import sys
import pandas as pd
import streamlit as st

# For reading and writing binary data, such as images or binary file formats.
from io import BytesIO

from Src.Modules.robby_sheet.table_tool import PandasAgent
from Src.Modules.File_Handling import Handle_Files
from Src.Modules.layout import Layout
from Src.Modules.utils import Utilities
from Src.Modules.sidebar import Sidebar


layout, sidebar, utils = Layout(), Sidebar(), Utilities()

# Loading the API key from .env file or the user input
user_openai_api_key = utils.load_api_key()
os.environ["OPENAI_API_KEY"] = user_openai_api_key

# In case OPENAI API KEY is not set up
if not user_openai_api_key:
    layout.show_api_key_missing()
else:
    """
    Set the reset_chat session state variable to False if it has not been previously set. 
    This variable controls whether or not the chat history is cleared when the user clicks the "Reset Chat" button.
    """
    st.session_state.setdefault("chat_history_cleared", False)
    uploaded_file = Handle_Files.file_upload(["csv", "xlsx"])

    # if uploaded_file:
    #     sidebar.about()
    #
    #     uploaded_file_content = BytesIO(uploaded_file.getvalue())
    #     if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or uploaded_file.type == "application/vnd.ms-excel":
    #         df = pd.read_excel(uploaded_file_content)
    #     else:
    #         df = pd.read_csv(uploaded_file_content)
    #
    #     st.session_state.df = df
    #
    #     if "chat_history" not in st.session_state:
    #         st.session_state["chat_history"] = []
    #     csv_agent = PandasAgent()
    #
    #     with st.form(key="query"):
    #
    #         query = st.text_input(
    #             "Ask [PandasAI](https://github.com/gventuri/pandas-ai) (look the pandas-AI read-me for how use it)",
    #             value="", type="default",
    #             placeholder="e-g : How many rows ? "
    #             )
    #         submitted_query = st.form_submit_button("Submit")
    #         reset_chat_button = st.form_submit_button("Reset Chat")
    #         if reset_chat_button:
    #             st.session_state["chat_history"] = []
    #     if submitted_query:
    #         result, captured_output = csv_agent.get_agent_response(df, query)
    #         cleaned_thoughts = csv_agent.process_agent_thoughts(captured_output)
    #         csv_agent.display_agent_thoughts(cleaned_thoughts)
    #         csv_agent.update_chat_history(query, result)
    #         csv_agent.display_chat_history()
    #     if st.session_state.df is not None:
    #         st.subheader("Current dataframe:")
    #         st.write(st.session_state.df)
