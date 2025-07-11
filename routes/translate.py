from fastapi import APIRouter, HTTPException
from models.schema import TranslateRequest, BulkTranslateRequest
from services.translator import translate_text, translate_bulk

router = APIRouter()

@router.post("/translate")
def translate(req: TranslateRequest):
    if len(req.text) > 1000:
        raise HTTPException(status_code=400, detail="Text exceeds 1000 characters.")
    return {"translated_text": translate_text(req.text, req.target_lang)}

@router.post("/translate/bulk")
def bulk_translate(req: BulkTranslateRequest):
    return {"translated_texts": translate_bulk(req.texts, req.target_lang)}
