# ufraw-batch

> 将相机的RAW文件转换为标准图像文件。
> 更多信息：<https://manned.org/ufraw-batch>。

- 简单地将RAW文件转换为JPEG：

`ufraw-batch --out-type=jpg {{输入文件}}`

- 简单地将RAW文件转换为PNG：

`ufraw-batch --out-type=png {{输入文件}}`

- 从RAW文件中提取预览图像：

`ufraw-batch --embedded-image {{输入文件}}`

- 将文件保存为不超过给定最大值MAX1和MAX2的大小：

`ufraw-batch --size=MAX1,MAX2 {{输入文件}}`