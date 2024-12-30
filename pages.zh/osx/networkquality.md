# 网络质量

> 通过连接互联网测量网络质量。
> 更多信息：<https://support.apple.com/101942>。

- 测试默认接口的网络质量：

`networkQuality`

- 顺序测试上传和下载速度，而不是并行测试：

`networkQuality -s`

- 测试指定的网络接口：

`networkQuality -I {{en0}}`

- 以详细输出测试网络质量：

`networkQuality -v`