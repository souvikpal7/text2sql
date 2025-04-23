import logging
from langgraph.graph import StateGraph, START, END
from text2sql.agent.states.graphstates import UserState

logger = logging.getLogger(__name__)

builder = StateGraph(UserState)

builder.add_node("access_info", user_access_info)

# Logic
builder.add_edge(START, "access_info")
builder.add_edge("access_info", END)
