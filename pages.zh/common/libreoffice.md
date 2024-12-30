# LibreOffice

> 强大且免费的办公套件 LibreOffice 的命令行接口。
> 更多信息：<https://www.libreoffice.org/>.

- 以只读模式打开一个或多个文件：

`libreoffice --view {{path/to/file1 path/to/file2 ...}}`

- 显示一个或多个文件的内容：

`libreoffice --cat {{path/to/file1 path/to/file2 ...}}`

- 使用指定的打印机打印文件：

`libreoffice --pt {{printer_name}} {{path/to/file1 path/to/file2 ...}}`

- 将当前目录下的所有 `.doc` 文件转换为 PDF：

`libreoffice --convert-to pdf *.doc`