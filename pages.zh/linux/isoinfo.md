# isoinfo

> 用于转储和验证 ISO 磁盘镜像的工具程序。
> 更多信息：<https://manned.org/isoinfo>.

- 列出 ISO 镜像中包含的所有文件：

`isoinfo -f -i {{path/to/image.iso}}`

- 从 ISO 镜像中提取指定文件并输出到 `stdout`：

`isoinfo -i {{path/to/image.iso}} -x {{/PATH/TO/FILE/INSIDE/ISO.EXT}}`

- 显示 ISO 磁盘镜像的头信息：

`isoinfo -d -i {{path/to/image.iso}}`