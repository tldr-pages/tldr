# Accelerate

> 一个使得可以在任何分布式配置中运行相同的 PyTorch 代码的库。
> 更多信息： <https://huggingface.co/docs/accelerate/index>。

- 打印环境信息：

`accelerate env`

- 交互式地创建配置文件：

`accelerate config`

- 打印使用不同数据类型运行 Hugging Face 模型的估计 GPU 内存成本：

`accelerate estimate-memory {{name/model}}`

- 测试一个 Accelerate 配置文件：

`accelerate test --config_file {{path/to/config.yaml}}`

- 使用 Accelerate 在 CPU 上运行一个模型：

`accelerate launch {{path/to/script.py}} {{--cpu}}`

- 使用 Accelerate 在多 GPU 上运行一个模型，使用 2 台机器：

`accelerate launch {{path/to/script.py}} --multi_gpu --num_machines 2`
