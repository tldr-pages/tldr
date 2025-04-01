# ddrescue

> 从损坏的块设备中恢复数据的工具。
> 更多信息：<https://www.gnu.org/software/ddrescue/manual/ddrescue_manual.html#Invoking-ddrescue>.

- 创建设备的镜像，并生成日志文件：

`sudo ddrescue {{/dev/sdb}} {{path/to/image.dd}} {{path/to/log.txt}}`

- 将磁盘 A 克隆到磁盘 B，并生成日志文件：

`sudo ddrescue {{[-f|--force]}} {{[-n|--no-scrape]}} {{/dev/sdX}} {{/dev/sdY}} {{path/to/log.txt}}`
