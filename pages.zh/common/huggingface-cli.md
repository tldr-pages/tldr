# huggingface-cli

> 与 Hugging Face Hub 交互。
> 登录、管理本地缓存、下载或上传文件。
> 更多信息：<https://huggingface.co/docs/huggingface_hub/guides/cli>。

- 登录 Hugging Face Hub：

`huggingface-cli login`

- 显示已登录用户的名称：

`huggingface-cli whoami`

- 注销：

`huggingface-cli logout`

- 打印环境信息：

`huggingface-cli env`

- 从仓库下载文件并打印出路径（省略文件名以下载整个仓库）：

`huggingface-cli download --repo-type {{repo_type}} {{repo_id}} {{filename1 filename2 ...}}`

- 将整个文件夹或文件上传到 Hugging Face：

`huggingface-cli upload --repo-type {{repo_type}} {{repo_id}} {{path/to/local_file_or_directory}} {{path/to/repo_file_or_directory}}`

- 扫描缓存以查看已下载的仓库及其磁盘使用情况：

`huggingface-cli scan-cache`

- 交互式删除缓存：

`huggingface-cli delete-cache`
