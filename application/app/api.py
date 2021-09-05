from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

act = FastAPI()

@act.get('/')
async def hello():
    return {'text': 'hello world!'}

class Data(BaseModel):
    string: str
    default_none: Optional[int] = None
    lists: List[int]

@act.post('/post')
async def declare_request_body(data: Data):
    return {'text': f'hello, {data.string}, {data.default_none}, {data.lists}'}
