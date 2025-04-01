# isisdl

> 用于柏林工业大学 ISIS 系统的下载工具。可以下载所有文件和视频。
> 更多信息：<https://github.com/Emily3403/isisdl>.

- 开始同步过程：

`isisdl`

- 将下载速度限制为 20 MiB/s 并使用 5 个线程下载：

`isisdl --download-rate {{20}} --max-num-threads {{5}}`

- 运行初始化配置向导：

`isisdl --init`

- 运行附加配置向导：

`isisdl --config`

- 开始完整的数据库同步并计算每个文件的校验和：

`isisdl --sync`

- 启动 ffmpeg 压缩下载的视频：

`isisdl --compress`