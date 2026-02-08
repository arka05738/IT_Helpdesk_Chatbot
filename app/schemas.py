from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    query: str = Field(
        ...,
        example="My laptop is overheating"
    )

class QueryResponse(BaseModel):
    response: str