# isisdl

> 一款用于柏林工业大学ISIS的下载工具。下载您在ISIS上的所有文件和视频。
> 更多信息：<https://github.com/Emily3403/isisdl>。

- 开始同步过程：

`isisdl`

- 将下载速度限制为每秒20 MiB，并使用5个线程下载：

`isisdl --download-rate {{20}} --max-num-threads {{5}}`

- 运行初始化配置向导：

`isisdl --init`

- 运行附加配置向导：

`isisdl --config`

- 启动数据库的完整同步并计算每个文件的校验和：

`isisdl --sync`

- 启动ffmpeg以压缩下载的视频：

`isisdl --compress`