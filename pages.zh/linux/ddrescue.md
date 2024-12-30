# ddrescue

> 数据恢复工具，用于从损坏的块设备中读取数据。
> 更多信息：<https://www.gnu.org/software/ddrescue/>.

- 创建设备的镜像，并生成日志文件：

`sudo ddrescue {{/dev/sdb}} {{path/to/image.dd}} {{path/to/log.txt}}`

- 将磁盘A克隆到磁盘B，并生成日志文件：

`sudo ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}} {{path/to/log.txt}}`