# aider

> 与您选择的 LLM 配对编程。
> 更多信息：<https://github.com/Aider-AI/aider>.

- 开始新项目或与现有代码库一起工作：

`aider --model {{model_name}} --api-key {{your_api_key}}`

- 向特定文件添加新功能或测试用例：

`aider {{path/to/file1 path/to/file2 ...}}`

- 描述一个错误并让 `aider` 修复它：

`aider {{path/to/file}} --describe "{{bug_description}}"`

- 重构特定文件中的代码：

`aider {{path/to/file}} --refactor`

- 更新文档：

`aider {{path/to/file}} --update-docs`

- 显示帮助：

`aider --help`
