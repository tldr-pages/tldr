# mknod

> 创建块或字符设备特殊文件。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/mknod-invocation.html>.

- 创建块设备：

`sudo mknod {{路径/到/设备文件}} b {{主设备号}} {{次设备号}}`

- 创建字符设备：

`sudo mknod {{路径/到/设备文件}} c {{主设备号}} {{次设备号}}`

- 创建先进先出（队列）设备：

`sudo mknod {{路径/到/设备文件}} p`

- 使用 SELinux 默认安全上下文创建设备文件：

`sudo mknod {{[-Z |--context=]}}{{路径/到/设备文件}} {{类型}} {{主设备号}} {{次设备号}}`
