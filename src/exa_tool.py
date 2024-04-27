import os
from exa_py import Exa
from langchain.agents import tool


class ExaSearchTool:

    @tool
    def search(query: str, include_domains=None, start_published_date=None):
        """Search for a webpage based on the query.
        Set the optional include_domains (list[str]) parameter to restrict the search to a list of domains.
        Set the optional start_published_date (str) parameter to restrict the search to documents published after the date (YYYY-MM-DD)."""

        return ExaSearchTool._exa().search_and_contents(
            f"{query}",
            use_autoprompt=True,
            num_results=5,
            include_domains=include_domains,
            start_published_date=start_published_date,
        )

    @tool
    def find_similar(url: str):
        """Search for webpages similar to a given URL.
        The url passed in should be a URL returned from `search`.
        """
        return ExaSearchTool._exa().find_similar(url, num_results=5)

    @tool
    def get_contents(ids: str):
        """Get the contents of a webpage.
        The ids must be passed in as a list, a list of ids returned from `search`.
        """
        ids = eval(ids)
        contents = str(ExaSearchTool._exa().get_contents(ids))
        print(contents)
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)

    def tools():
        return [ExaSearchTool.search, ExaSearchTool.find_similar, ExaSearchTool.get_contents]

    def _exa():
        return Exa(api_key=os.environ["EXA_API_KEY"])
