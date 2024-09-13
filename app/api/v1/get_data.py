from fastapi import APIRouter

from app.model.models import ResponseModel, ExporterManage
from core.db import SessionDep
from utils.constant import COMPONENT_CONSTANT

router = APIRouter()


@router.get("/component/{component_name}", response_model=ResponseModel)
async def get_component_data(component_name: str, db: SessionDep):
    """
    通过组件名称，获取采集到的组件指标
    """
    component = db.query(ExporterManage).filter(ExporterManage.name == component_name).first()
    if component:
        component_metrics = await COMPONENT_CONSTANT.get(component.name.upper())(component).metrics()
    else:
        component_metrics = ""
    return ResponseModel(data=component_metrics)

