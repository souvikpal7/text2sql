from pydantic import BaseModel
from typing import Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


class UserState(BaseModel):
    user_name: str
    user_role: str
    table_access: list
    messages: Annotated[list[AnyMessage], add_messages]
