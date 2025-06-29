# fastapi

> 用于运行 FastAPI 应用的 CLI 工具，底层使用 Uvicorn。
> 更多信息：<https://fastapi.tiangolo.com/tutorial/cli/>.

- 使用自动重新加载运行 FastAPI 应用（用于开发）：

`fastapi run {{main.py}} --reload`

- 使用 `dev` 命令在开发或生产模式下运行应用：

`fastapi dev {{main.py}}`

- 指定运行的主机和端口：

`fastapi run {{main.py}} --host {{0.0.0.0}} --port {{8000}}`

- 设置应用变量名（如果不是 `app`）或指定自定义应用目录：

`fastapi run {{main.py}} --app-dir {{path/to/app}} --app {{custom_app_name}}`

- 显示全局帮助信息：

`fastapi --help`

- 显示子命令的帮助信息：

`fastapi run --help`
