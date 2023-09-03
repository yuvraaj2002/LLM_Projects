import streamlit as st


# Setting the configuration of Streamlit page
st.set_page_config(layout="wide", page_icon="💬", page_title="Chat-Bot 🤖")


# Mentioning my social media profile links
with st.sidebar.expander("📬 Connect With Me"):

    st.write("**GitHub:**","[yvann-hub/Robby-chatbot](https://github.com/yvann-hub/Robby-chatbot)")
    st.write("**Medium:** ""[@yvann-hub](https://medium.com/@yvann-hub)")
    st.write("**Twitter:** [@yvann_hub](https://twitter.com/yvann_hub)")
    st.write("**Mail** : barbot.yvann@gmail.com")
    st.write("**Application created by Yuvraj Singh**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Robby, your data-aware assistant 🤖</h1>
    """,unsafe_allow_html=True)

# st.markdown("---")


# Description about the project
st.markdown(
    """ 
    <p style='text-align:center;'>Developing a CSV Chatbot powered by OpenAI's language models and LangChain 
    technology, this project aims to create an intelligent 
    conversational agent capable of seamlessly interacting with CSV data. Leveraging cutting-edge AI capabilities, it will enable users to effortlessly query, analyze, 
    and manipulate data from CSV files through natural language, revolutionizing data-driven decision-making.</p>
    """,
    unsafe_allow_html=True)
st.markdown("---")


# Tools and technologies used
st.subheader("️🛠️ Tools and technologies Used")
st.write("""
- **OpenAI Language Models**: Utilizing OpenAI's advanced language models for natural language understanding and generation.
- **LangChain Integration:** Integrating LangChain technology for efficient handling and processing of CSV data within the chatbot.
- **CSV Data Parsing** Implementing CSV data parsing libraries or custom solutions for extracting and working with 
structured data.
""")



# My social media links
st.markdown("---")
st.subheader("❤️ Tools and technologies Used")
st.write("""
- **GitHub**: [yvann-hub/Robby-chatbot](https://github.com/yvann-hub/Robby-chatbot)
- **HashNode**: [@yvann_hub](https://twitter.com/yvann_hub)
- **Twitter**: [@yvann_hub](https://twitter.com/yvann_hub)
- **Email**: barbot.yvann@gmail.com
""")
