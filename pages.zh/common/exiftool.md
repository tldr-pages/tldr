# exiftool

> 读取和写入文件中的元信息。
> 更多信息：<https://exiftool.org>.

- 打印指定文件的 EXIF 元数据：

`exiftool {{path/to/file}}`

- 从指定文件中删除所有 EXIF 元数据：

`exiftool -All= {{path/to/file1 path/to/file2 ...}}`

- 从指定图像文件中删除 GPS EXIF 元数据：

`exiftool "-gps*=" {{path/to/image1 path/to/image2 ...}}`

- 从指定图像文件中删除所有 EXIF 元数据，然后重新添加颜色和方向的元数据：

`exiftool -All= -tagsfromfile @ -colorspacetags -orientation {{path/to/image1 path/to/image2 ...}}`

- 将目录中所有照片的拍摄日期向后移动 1 小时：

`exiftool "-AllDates+=0:0:0 1:0:0" {{path/to/directory}}`

- 将当前目录中所有 JPEG 照片的拍摄日期向前移动 1 天 2 小时：

`exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg`

- 仅更改 `DateTimeOriginal` 字段，减去 1.5 小时，不保留备份：

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- 基于 `DateTimeOriginal` 字段递归重命名目录中的所有 JPEG 照片：

`exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e {{path/to/directory}} -r -ext jpg`