from crewai import Task, Agent
from crewai.tasks.task_output import TaskOutput
from typing import List
import streamlit as st


class Tasks():

    def __init__(self, topic, agents: List[Agent]) -> None:
        self.topic: str = topic
        self.agents = agents

    def trend_hunting_task(self) -> Task:
        return Task(
            description=f"""Identify the top 5 most important trending topics in the {
                self.topic} area""",
            expected_output=f"""A bullet list summary of the top 5 most important {
                self.topic} news""",
            agent=self.agents[0]
        )

    def research_task(self) -> Task:
        return Task(
            description=f"""Research and give some insights about the latest trending topics in {
                self.topic} area""",
            expected_output=f"""A comprehensive research report on given trend""",
            agent=self.agents[1],
            context=[self.trend_hunting_task()]
        )

    def content_planning_task(self) -> Task:
        return Task(
            description="Create a completed content plan for engaging linkedIn posts",
            expected_output=f"""A comprehensive 5 days content plan on given trends in a markdown format""",
            agent=self.agents[2],
            context=[self.trend_hunting_task(), self.research_task()],
            callback=self._writeTaskResult
        )

    def post_write_task(self) -> Task:
        return Task(
            description="Write engaging LinkedIn posts based on the provided content plan",
            expected_output=f"""Engaging posts in a markdown format (Post #1, Post #2...) with emojis""",
            agent=self.agents[3],
            context=[self.content_planning_task(), self.research_task()],
            output_file=f'{"-".join(self.topic.split())}-task-output.md'
        )

    def _writeTaskResult(self, task: TaskOutput):
        st.divider()
        st.subheader("Content Plan")
        st.markdown(task.raw_output)

    def getTasks(self):
        return [self.trend_hunting_task(), self.research_task(), self.content_planning_task(), self.post_write_task()]
