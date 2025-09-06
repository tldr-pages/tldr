# ufraw-batch

> 将来自相机的 RAW 文件转换为标准图像文件。
> 更多信息：<https://manned.org/ufraw-batch>.

- 简单地将 RAW 文件转换为 JPEG：

`ufraw-batch --out-type=jpg {{（或多个）输入文件}}`

- 简单地将 RAW 文件转换为 PNG：

`ufraw-batch --out-type=png {{（或多个）输入文件}}`

- 从 RAW 文件中提取预览图像：

`ufraw-batch --embedded-image {{（或多个）输入文件}}`

- 将文件保存为不超过给定的最大尺寸 MAX1 和 MAX2：

`ufraw-batch --size=MAX1,MAX2 {{（或多个）输入文件}}`
