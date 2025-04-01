# gh skyline

> 生成 GitHub 贡献历史记录的 3D 模型。
> 默认情况下，它将在当前目录创建一个 `{username}-{year}-github-skyline.stl` 文件。
> 更多信息：<https://github.com/github/gh-skyline>.

- 为当前年份和已认证用户生成一个天空线 STL 文件：

`gh skyline`

- 为特定用户和年份生成一个天空线：

`gh skyline {{[-u|--user]}} {{username}} {{[-y|--year]}} {{year}}`

- 为一系列年份生成一个天空线：

`gh skyline {{[-u|--user]}} {{username}} {{[-y|--year]}} {{first_year}}-{{last_year}}`

- 生成完整的天空线（从用户加入年份到当前年份）：

`gh skyline {{[-u|--user]}} {{username}} {{[-f|--full]}}`

- 启用调试日志：

`gh skyline {{[-d|--debug]}}`

- 生成天空线并指定输出文件路径：

`gh skyline {{[-o|--output]}} {{path/to/output_file.stl}}`

- 打开特定用户的 GitHub 个人资料页面：

`gh skyline {{[-u|--user]}} {{username}} {{[-w|--web]}}`

- 显示帮助：

`gh skyline {{[-h|--help]}}`
