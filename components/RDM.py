from app.model.models import ExporterManage
from components.base_componrnt import BaseComponent
from typing import Union
from prometheus_client import Gauge, CollectorRegistry, generate_latest
from utils.utils import get_status_code


class RDM(BaseComponent):
    def __init__(self, cfg):
        super().__init__()
        self.cfg: ExporterManage = cfg
        self.url = self.cfg.address
        self.registry = CollectorRegistry()
        self.service_status = Gauge('rdm_service_status', 'Current status of the service (0=up, 1=down)',
                                    registry=self.registry)

    async def metrics(self) -> Union[str, None]:
        """
        目标指标数据
        """
        try:
            status_code = await self.status()
            self.service_status.set(status_code)
            metric_data = generate_latest(self.registry)
            return metric_data.decode('utf-8')
        except Exception as e:
            # 记录错误日志
            print(f"Error in metrics: {str(e)}")
            return None

    async def status(self) -> int:
        """
        此目标状态，目标未运行、不存在时，返回为空
        (0=up, 1=down)
        """
        try:
            return 0 if await get_status_code(self.url) == 200 else 1
        except Exception as e:
            # 记录错误日志
            print(f"Error in status check: {str(e)}")
            return 1
