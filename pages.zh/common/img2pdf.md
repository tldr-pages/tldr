# img2pdf

> 无损地将位图图像转换为 PDF 文件。
> 支持的图像格式包括：GIF、JPEG、JPEG2000、PNG、GIF 和 TIFF。
> 更多信息：<https://gitlab.mister-muffin.de/josch/img2pdf>。

- 将一个或多个图像转换为单个 PDF，每个图像位于自己的页面上：

`img2pdf {{path/to/image1.ext path/to/image2.ext ...}} --output {{path/to/file.pdf}}`

- 仅将多帧图像的第一页转换为 PDF：

`img2pdf {{path/to/file.gif}} --first-frame-only --output {{path/to/file.pdf}}`

- 自动调整图像方向，使用特定的横向页面大小，并设置水平和垂直方向上的边框大小：

`img2pdf {{path/to/image.ext}} --auto-orient --pagesize {{A4^T}} --border {{2cm}}:{{5.1cm}} --output {{path/to/file.pdf}}`

- 仅缩小较大图像，使其适应特定尺寸的页面内的指定矩形：

`img2pdf {{path/to/image.ext}} --pagesize {{30cm}}x{{20cm}} --imgsize {{10cm}}x{{15cm}} --fit {{shrink}} --output {{path/to/file.pdf}}`

- 将图像转换为 PDF，并为生成的文件指定元数据：

`img2pdf {{path/to/image.ext}} --title {{title}} --author {{author}} --creationdate {{1970-01-31}} --keywords {{keyword1 keyword2}} --subject {{subject}} --output {{path/to/file.pdf}}`
