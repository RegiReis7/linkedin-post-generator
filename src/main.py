import streamlit as st
import os
from agents import Agents
from tasks import Tasks
from crewai import Crew
from crewai.process import Process
from dotenv import load_dotenv

load_dotenv()


def main():
    st.title("Trend Hunter")

    with st.sidebar:

        st.subheader("API KEYS")

        # Input field for Tavily API key
        exa_api_key = st.text_input(
            "Enter your EXA API key:", type="password")

    topic = st.text_input("Enter the topic you want to search for:")

    if st.button("HUNT!"):

        with st.spinner('PROCESSING'):

            os.environ["EXA_API_KEY"] = exa_api_key
            os.environ["OPENAI_API_KEY"] = os.environ.get("MISTRAL_API_KEY")
            os.environ["OPENAI_API_BASE"] = "https://api.mistral.ai/v1"
            os.environ["OPENAI_MODEL_NAME"] = "mistral-small-2402"

            agents = Agents(topic)

            tasks = Tasks(topic, agents.getAgents())

            crew = Crew(
                agents=agents.getAgents(),
                tasks=tasks.getTasks(),
                process=Process.sequential)

            result = crew.kickoff()

            st.divider()
            st.success("HUNT COMPLETE!")
            st.markdown(result)


if __name__ == "__main__":
    main()
