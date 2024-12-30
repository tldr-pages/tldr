# accelerate

> 一个库，可以在任何分布式配置中运行相同的PyTorch代码。
> 更多信息：<https://huggingface.co/docs/accelerate/index>。

- 打印环境信息：

`accelerate env`

- 交互式创建配置文件：

`accelerate config`

- 打印使用不同数据类型运行Hugging Face模型的估计GPU内存成本：

`accelerate estimate-memory {{name/model}}`

- 测试Accelerate配置文件：

`accelerate test --config_file {{path/to/config.yaml}}`

- 使用Accelerate在CPU上运行模型：

`accelerate launch {{path/to/script.py}} {{--cpu}}`

- 使用Accelerate在多GPU上运行模型，包含2台机器：

`accelerate launch {{path/to/script.py}} --multi_gpu --num_machines 2`