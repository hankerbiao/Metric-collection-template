# 组件基本信息，统一采集组件的接口

from abc import ABC, abstractmethod
from typing import Union


class BaseComponent(ABC):
    @abstractmethod
    def metrics(self) -> Union[str, None]:
        """
        返回指标细节
        """
        pass

    @abstractmethod
    def status(self) -> bool:
        """
        目标对象状态
        """
        pass
