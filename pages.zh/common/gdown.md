# gdown

> 从 Google Drive 和其他 URL 下载文件。
> 更多信息：<https://github.com/wkentaro/gdown>。

- 从 URL 下载文件：

`gdown {{url}}`

- 使用文件 ID 下载文件：

`gdown {{file_id}}`

- 使用模糊文件 ID 提取下载（也适用于 <https://docs.google.com> 链接）：

`gdown --fuzzy {{url}}`

- 使用文件夹 ID 或完整 URL 下载文件夹：

`gdown {{folder_id|url}} -O {{path/to/output_directory}} --folder`

- 下载 tar 压缩包，将其写入 `stdout` 并解压：

`gdown {{tar_url}} -O - --quiet | tar xvf -`
