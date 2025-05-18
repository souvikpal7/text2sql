import logging
from langchain import hub
from langgraph.graph import StateGraph, START, END
from langgraph.graph import MessagesState
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from text2sql2.agent.metadata.DataBases import SakilaDB
from langchain.chat_models import init_chat_model

# class BaseDB:
#     def __init__(self, db_url):
#         self.conn = sqlite3.connect(db_url)

# def SakilaDB(db_path=None, db_type=None):
#     if not db_path:
#         db_path = "/mnt/c/Users/conta/Downloads/Saklia/sqlite-sakila.db"
#     if not db_type:
#         db_type = "sqlite"

#     db_uri = f"{db_type}:///{db_path}"
#     db = SQLDatabase.from_uri(db_uri)
#     return db


# logger = logging.getLogger(__name__)

# builder = StateGraph(UserState)

# builder.add_node("access_info", user_access_info)

# # Logic
# builder.add_edge(START, "access_info")
# builder.add_edge("access_info", END)

class SQLReactAgent:

    def __init__(self, db, model_name="gpt-4o-mini", model_provider="openai"):
        self.db = db
        self.llm = init_chat_model(model_name, model_provider=model_provider)
        self.builder = StateGraph(MessagesState)
        toolkit = SQLDatabaseToolkit(db=db, llm=self.llm)
        self.tools = toolkit.get_tools()
        prompt_template = hub.pull("langchain-ai/sql-agent-system-prompt")


        system_message = prompt_template.format(dialect="SQLite", top_k=5)
        self.agent_executor = create_react_agent(
            self.llm,
            self.tools,
            prompt=system_message
            )

    def __call__(self, *args, **kwds):
        while True:
            question = input("Enter User Question: ")
            if question.lower().strip() in ["q", "quit"]:
                break

            for step in self.agent_executor.stream(
                {"messages": [{"role": "user", "content": question}]},
                stream_mode="values",
            ):
                step["messages"][-1].pretty_print()
