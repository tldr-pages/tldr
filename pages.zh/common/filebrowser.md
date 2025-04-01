# filebrowser

> 简单的 HTTP 网页服务器，用于管理和浏览文件和目录。
> 更多信息：<https://filebrowser.org>.

- 启动一个新服务器实例，服务当前目录：

`filebrowser`

- 启动一个新服务器实例，服务指定的根目录：

`filebrowser {{[-r|--root]}} {{path/to/directory}}`

- 启动一个实例，使用不同的主机地址（默认为 `127.0.0.1`）和端口（默认为 `8080`）：

`filebrowser {{[-a|--address]}} {{host}} {{[-p|--port]}} {{port}} {{[-r|--root]}} {{path/to/directory}}`

- 启动一个实例，使用指定的配置文件，并将应用程序数据库存储在特定位置（默认为当前目录下的 `filebrowser.db`）：

`filebrowser {{[-c|--config]}} {{path/to/file}} {{[-d|--database]}} {{path/to/database.db}} {{[-r|--root]}} {{path/to/directory}}`

- 设置首次创建实例时默认的用户名和密码（默认均为 `admin`）：

`filebrowser --username {{username}} --password {{password}} {{[-r|--root]}} {{path/to/directory}}`

- 设置生成缩略图时使用的最大图像处理器数量（默认为 `4`）：

`filebrowser --img-processors {{4}} {{[-r|--root]}} {{path/to/directory}}`

- 禁用图像缩略图和命令运行器功能，限制托管脚本文件在应用程序内的执行：

`filebrowser --disable-exec --disable-thumbnails {{[-r|--root]}} {{path/to/directory}}`

- 禁用图像预览的调整大小以及通过读取文件头部来检测文件类型：

`filebrowser --disable-preview-resize --disable-type-detection-by-header {{[-r|--root]}} {{path/to/directory}}`