# magick identify

> 描述图像文件的格式和特征。
> 另请参见：`magick`。
> 更多信息：<https://imagemagick.org/script/identify.php>。

- 描述图像的格式和基本特征：

`magick identify {{path/to/image}}`

- 描述图像的格式和详细特征：

`magick identify -verbose {{path/to/image}}`

- 收集当前目录中所有JPEG文件的尺寸并将其保存到CSV文件中：

`magick identify -format "{{%f,%w,%h\n}}" {{*.jpg}} > {{path/to/filelist.csv}}`