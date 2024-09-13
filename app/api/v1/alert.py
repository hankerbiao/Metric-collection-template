from fastapi import APIRouter, Request
import json

from app.model.models import ResponseModel

router = APIRouter()


@router.post("/webhook")
async def receive_alert(request: Request):
    try:
        body = await request.body()
        # 解析JSON数据
        alert_data = json.loads(body)
        print(alert_data)
    except Exception as e:
        return ResponseModel(data=e)
