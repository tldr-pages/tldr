# jpegoptim

> 优化JPEG图像。
> 更多信息：<https://github.com/tjko/jpegoptim>。

- 优化一组JPEG图像，保留所有相关数据：

`jpegoptim {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- 优化JPEG图像，去除所有非必要数据：

`jpegoptim --strip-all {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- 强制输出图像为渐进式：

`jpegoptim --all-progressive {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- 强制输出图像具有固定的最大文件大小：

`jpegoptim --size={{250k}} {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`