# duti

> 在MacOS上为文档类型和网页设置默认打开的应用程序.

- 将Safari设置为HTML文档的默认打开程序:

`duti -s {{com.apple.Safari}} {{public.html}} all`

- 将vlc设置为扩展名为.m4v的文件的默认查看器:

`duti -s {{org.videolan.vlc}} {{m4v}} viewer`

- 将Finder设置为 ftp:// URL 访问的应用:

`duti -s {{com.apple.Finder}} {{ftp}}`

- 显示有关给定扩展名的默认应用程序的信息:

`duti -x {{ext}}`

- 显示给定的 UTI 对应默认的处理程序:

`duti -d {{uti}}`

- 显示给定 UTI 对应所有的处理程序:

`duti -l {{uti}}`
