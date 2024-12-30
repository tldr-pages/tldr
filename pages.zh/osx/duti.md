# duti

> 在 macOS 上为文档类型和 URL 方案设置默认应用程序。
> 更多信息：<https://github.com/moretension/duti>。

- 将 Safari 设置为 HTML 文档的默认处理程序：

`duti -s {{com.apple.Safari}} {{public.html}} all`

- 将 VLC 设置为 `.m4v` 扩展名文件的默认查看器：

`duti -s {{org.videolan.vlc}} {{m4v}} viewer`

- 将 Finder 设置为 ftp:// URL 方案的默认处理程序：

`duti -s {{com.apple.Finder}} "{{ftp}}"`

- 显示给定扩展名的默认应用程序信息：

`duti -x {{ext}}`

- 显示给定 UTI 的默认处理程序：

`duti -d {{uti}}`

- 显示给定 UTI 的所有处理程序：

`duti -l {{uti}}`