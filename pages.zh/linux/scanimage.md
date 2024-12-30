# scanimage

> 使用扫描仪访问现在简单（Scanner Access Now Easy）API 扫描图像。
> 更多信息：<http://sane-project.org/man/scanimage.1.html>。

- 列出可用的扫描仪，以确保目标设备已连接并被识别：

`scanimage -L`

- 扫描图像并将其保存为文件：

`scanimage --format={{pnm|tiff|png|jpeg}} > {{path/to/new_image}}`