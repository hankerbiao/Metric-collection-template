from fastapi import APIRouter

from app.api.v1 import get_data,alert
api_route = APIRouter()
api_route.include_router(get_data.router, tags=["获取日期测试"])
api_route.include_router(alert.router, tags=["告警消息处理"])