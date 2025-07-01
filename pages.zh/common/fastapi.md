# fastapi

> 运行 FastAPI 应用的命令行工具，底层使用 Uvicorn。
> 更多信息：<https://manned.org/fastapi>.

- 使用自动重载运行 FastAPI 应用（用于开发）：

`fastapi run {{路径/文件.py}} --reload`

- 在开发模式下运行应用：

`fastapi dev {{路径/文件.py}}`

- 指定运行的主机和端口：

`fastapi run {{路径/文件.py}} --host {{主机地址}} --port {{端口}}`

- 设置应用变量名（如果不是 `app`）或指定自定义应用目录：

`fastapi run {{路径/文件.py}} --app-dir {{路径/到/应用}} --app {{自定义_app_名称}}`

- 显示帮助信息：

`fastapi --help`

- 显示子命令的帮助信息：

`fastapi {{子命令}} --help`
