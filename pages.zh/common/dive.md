# dive

> 探索 Docker 镜像、层内容，并发现缩小它的方法。
> 更多信息：<https://github.com/wagoodman/dive>。

- 分析一个 Docker 镜像：

`dive {{your_image_tag}}`

- 构建一个镜像并开始分析：

`dive build -t {{some_tag}}`