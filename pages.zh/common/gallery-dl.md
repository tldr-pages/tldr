# gallery-dl

> 从多个图像托管网站下载图像画廊和集合。
> 更多信息: <https://github.com/mikf/gallery-dl>。

- 从指定的 URL 下载图像：

`gallery-dl "{{url}}"`

- 将图像保存到特定目录：

`gallery-dl --destination {{path/to/directory}} "{{url}}"`

- 从您的网页浏览器中获取现有的 cookies（对需要登录的网站很有用）：

`gallery-dl --cookies-from-browser {{browser}} "{{url}}"`

- 从支持使用用户名和密码进行身份验证的网站获取图像的直接 URL：

`gallery-dl --get-urls --username {{username}} --password {{password}} "{{url}}"`

- 按章节编号和语言过滤漫画章节：

`gallery-dl --chapter-filter "{{10 <= chapter < 20}}" --option "lang={{language_code}}" "{{url}}"`