from sqlmodel import SQLModel, Field
from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class ExporterManage(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, description="唯一标识符")
    name: Optional[str] = Field(default=None, nullable=True)
    address: Optional[str] = Field(default=None, nullable=True)
    username: Optional[str] = Field(default=None, nullable=True)
    password: Optional[str] = Field(default=None, nullable=True)
    parameter: Optional[str] = Field(default=None, nullable=True)
    description: Optional[str] = Field(default=None, nullable=True)


class ResponseModel(SQLModel, Generic[T]):
    """
    通用响应模型，用于标准化 API 响应格式
    """

    status: bool = Field(default=True, description="请求是否成功")
    code: int = Field(default=200, description="状态码")
    data: Optional[T] = Field(default=None, description="响应数据")
    message: str = Field(default="成功", description="描述信息")

    def __repr__(self):
        return (
            f"<ResponseModel(status={self.status}, code={self.code}, "
            f"data={self.data}, message={self.message})>"
        )
