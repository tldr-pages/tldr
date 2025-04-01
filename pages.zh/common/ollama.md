# ollama

> 大型语言模型运行器。
> 可用模型列表：<https://ollama.com/library>。
> 更多信息：<https://github.com/ollama/ollama>。

- 启动运行其他命令所需的守护进程：

`ollama serve`

- 运行模型并与其进行聊天：

`ollama run {{model}}`

- 使用单个提示运行模型：

`ollama run {{model}} {{prompt}}`

- 列出已下载的模型：

`ollama list`

- 拉取/更新特定模型：

`ollama pull {{model}}`

- 列出正在运行的模型：

`ollama ps`

- 删除模型：

`ollama rm {{model}}`

- 从 `Modelfile` 创建模型：

`ollama create {{new_model_name}} {{[-f|--file]}} {{path/to/Modelfile}}`