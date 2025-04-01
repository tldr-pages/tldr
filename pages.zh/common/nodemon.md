# nodemon

> 监视文件并在检测到文件变化时自动重启 Node 应用程序。
> 更多信息：<https://nodemon.io>.

- 执行指定文件并监视特定文件的变化:

`nodemon {{path/to/file.js}}`

- 手动重启 nodemon（注意，nodemon 必须已经处于活动状态才能执行此操作）:

`rs`

- 忽略特定文件:

`nodemon --ignore {{path/to/file_or_directory}}`

- 传递参数给 Node 应用程序:

`nodemon {{path/to/file.js}} {{arguments}}`

- 如果不是 nodemon 参数，则传递参数给 Node 本身（例如 `--inspect`）:

`nodemon {{arguments}} {{path/to/file.js}}`

- 运行任意非 Node 脚本:

`nodemon --exec "{{command_to_run_script}} {{options}}" {{path/to/script}}`

- 运行 Python 脚本:

`nodemon --exec "python {{options}}" {{path/to/file.py}}`