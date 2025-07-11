from pydantic import BaseModel
from typing import List

class TranslateRequest(BaseModel):
    text: str
    target_lang: str

class BulkTranslateRequest(BaseModel):
    texts: List[str]
    target_lang: str
