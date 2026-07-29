# aha

> 将 ANSI 转义序列转换为 HTML。
> 更多信息：<https://manned.org/aha>。

- 将终端输出转换为 HTML：

`{{颜色命令}} | aha > {{路径/到/output}}.html`

- 从文件读取而不是 `stdin`：

`aha -f {{路径/到/input.txt}} > {{路径/到/output}}.html`

- 转换为黑色背景的 HTML：

`{{颜色命令}} | aha {{[-b|--black]}} > {{路径/到/output}}.html`

- 转换为粉色背景的 HTML 并设置文档标题：

`{{颜色命令}} | aha {{[-p|--pink]}} {{[-t|--title]}} "{{标题}}" > {{路径/到/output}}.html`

- 向 HTML 输出添加 CSS 文件：

`{{颜色命令}} | aha {{[-c|--css]}} {{路径/到/style}}.css > {{路径/到/output}}.html`

- 启用自动换行以防止水平滚动：

`{{颜色命令}} | aha {{[-w|--word-wrap]}} > {{路径/到/output}}.html`

- 显示帮助：

`aha {{[-h|--help]}}`
