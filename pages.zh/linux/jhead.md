# jhead

> 图像时间戳和EXIF数据操作。
> 更多信息：<https://www.sentex.net/~mwandel/jhead/usage.html>。

- 显示所有EXIF数据：

`jhead {{path/to/image.jpg}}`

- 将文件的日期和时间设置为EXIF创建日期（文件创建日期将被更改）：

`jhead -ft {{path/to/image.jpg}}`

- 将EXIF时间设置为文件的日期和时间（EXIF数据将被更改）：

`jhead -dsft {{path/to/image.jpg}}`

- 根据EXIF创建日期将所有JPEG文件重命名为`YYYY_MM_DD-HH_MM_SS.jpg`：

`jhead -n%Y_%m_%d-%H_%M_%S *.jpg`

- 根据EXIF方向标签无损旋转所有JPEG图像90、180或270度：

`jhead -autorot *.jpg`

- 更新所有EXIF时间戳（格式：+- 时:分:秒）（例如：忘记更改相机的时区 - 从时间戳中减去1小时）：

`jhead -ta-1:00:00 *.jpg`

- 删除所有EXIF数据（包括缩略图）：

`jhead -purejpg {{path/to/image.jpg}}`