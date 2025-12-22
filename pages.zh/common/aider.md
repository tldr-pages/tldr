# aider

> 使用你选择的 LLM 进行结对编程。
> 更多信息：<https://github.com/Aider-AI/aider>.

- 启动一个新项目，或在现有代码库上工作：

`aider --model {{模型名称}} --api-key {{你的_API_密钥}}`

- 向指定文件添加新功能或测试用例：

`aider {{路径/到/文件1 路径/到/文件2 ...}}`

- 描述一个 Bug，并让 `aider` 修复它：

`aider {{路径/到/文件}} --describe "{{Bug_描述}}"`

- 重构指定文件中的代码：

`aider {{路径/到/文件}} --refactor`

- 更新文档：

`aider {{路径/到/文件}} --update-docs`

- 显示帮助信息：

`aider --help`
