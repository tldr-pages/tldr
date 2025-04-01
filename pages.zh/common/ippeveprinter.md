# ippeveprinter

> 一个简单的 IPP Everywhere 打印机服务器。
> 另见: `ippeveps`, `ippevepcl`。
> 更多信息: <https://openprinting.github.io/cups/doc/man-ippeveprinter.html>。

- 使用特定的服务名称运行服务器:

`ippeveprinter "{{service_name}}"`

- 从 PPD 文件加载打印机属性:

`ippeveprinter -P {{path/to/file.ppd}} "{{service_name}}"`

- 每当作业发送到服务器时运行 `file` 命令:

`ippeveprinter -c {{/usr/bin/file}} "{{service_name}}"`

- 指定将保存打印文件的目录（默认情况下，是在用户临时目录下的一个目录）:

`ippeveprinter -d {{spool_directory}} "{{service_name}}"`

- 保留而不是删除 spool 目录中的打印文档:

`ippeveprinter -k "{{service_name}}"`

- 指定打印机速度，单位为页/分钟（默认为 10）:

`ippeveprinter -s {{speed}} "{{service_name}}"`