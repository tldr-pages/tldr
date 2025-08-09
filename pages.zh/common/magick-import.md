# magick import

> 捕获某些或全部 X server 屏幕上的内容，并保存至图片文件当中。
> 另见：`magick`。
> 更多信息：<https://imagemagick.org/script/import.php>.

- 捕获整个 X server 屏幕，保存为 PostScript 文件：

`magick import -window root {{路径/到/输出文件.ps}}`

- 捕获远程 X server 屏幕，保存为 PNG 图片：

`magick import -window root -display {{remote_host}}:{{screen}}.{{display}} {{路径/到/输出文件.png}}`

- 用 `xwininfo` 中列出的窗口 ID 对特定窗口进行捕获，保存为 JPEG 图片：

`magick import -window {{窗口 ID}} {{路径/到/输出图片.jpg}}`
