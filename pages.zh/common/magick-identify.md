# magick identify

> 描述图像文件的格式和特征。
> 参见：`magick`。
> 更多信息：<https://imagemagick.org/script/identify.php>。

- 描述图像的格式和基本特征：

`magick identify {{path/to/image}}`

- 详细描述图像的格式和特征：

`magick identify -verbose {{path/to/image}}`

- 收集当前目录中所有 JPEG 文件的尺寸，并保存到 CSV 文件中：

`magick identify -format "{{%f,%w,%h\n}}" {{*.jpg}} > {{path/to/filelist.csv}}`