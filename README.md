# LinkedIn Post Generator using CrewAI

This project leverages CrewAI, a cutting-edge framework for orchestrating role-playing autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to seamlessly work together, tackling complex tasks.

## Overview

The LinkedIn Post Generator utilizes Streamlit for the interface and poetry as the main package manager, with Python version 3.12.1.

## Agents

### 1. Trend Hunter

The Trend Hunter agent gathers the latest trending topics about a given topic.

### 2. Researcher

The Researcher agent conducts independent investigations within different areas.

### 3. Content Planner

The Content Planner agent develops a content calendar that drives engagement with our target audience related to a given topic.

### 4. Post Writer

The Post Writer agent crafts posts that drive engagement with our target audience related to the given topic.

## Dependencies

This project relies on Mistral AI as the main language model, thus requiring an environment variable: `MISTRAL_API_KEY`.

```
export MISTRAL_API_KEY=your_mistral_api_key_here
```

## Usage

To run the LinkedIn Post Generator, follow these steps:

1. Install the necessary dependencies using poetry:

```bash
poetry install
```

2. Set up the Mistral API key:

```bash
export MISTRAL_API_KEY=your_mistral_api_key_here
```

3. Run the Streamlit interface:

```bash
streamlit run app.py
```

4. Follow the prompts in the interface to utilize the different agents and generate engaging LinkedIn posts.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.