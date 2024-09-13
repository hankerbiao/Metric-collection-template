# Prometheus 自定义指标采集模板

基于FastAPI的Prometheus自定义指标采集模板，提供简单高效的方式来收集和暴露自定义指标。

## 特性

- 使用FastAPI构建高性能API
- 集成Prometheus客户端，便于指标收集
- 简单易用的自定义指标定义方式
- 支持多种指标类型（如Counter, Gauge, Histogram等）
  
  ## 快速开始
  
  ### 前置条件
  
- Python 3.8+
- pip
  
  ### 安装步骤
  

1. 克隆仓库：

```bash
git clone https://github.com/hankerbiao/Metric-collection-template.git
cd Metric-collection-templatee
```

2. 创建环境、安装依赖
  

```bash
python -m venv venv
source venv/bin/activate
pip install poetry
poetry install
python main.py
```