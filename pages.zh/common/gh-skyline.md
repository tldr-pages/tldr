# gh skyline

> 生成您的 GitHub 贡献历史的 3D 模型。
> 默认情况下，它将在当前目录中创建一个 `{username}-{year}-github-skyline.stl` 文件。
> 更多信息：<https://github.com/github/gh-skyline>。

- 为当前年份和已认证用户生成天际线 STL 文件：

`gh skyline`

- 为特定的 [u]ser 和 [y]ear 生成天际线：

`gh skyline --user {{username}} --year {{year}}`

- 为一系列 [y]ears 生成天际线：

`gh skyline --user {{username}} --year {{first_year}}-{{last_year}}`

- 生成一个 [f]ull 天际线（从用户加入年份到当前年份）：

`gh skyline --user {{username}} --full`

- 启用 [d]ebug 日志记录：

`gh skyline --debug`

- 生成天际线并指定 [o]utput 文件路径：

`gh skyline --output {{path/to/output_file.stl}}`

- 打开特定 [u]ser 的 GitHub 个人资料：

`gh skyline --user {{username}} --web`

- 显示 [h]elp：

`gh skyline --help`