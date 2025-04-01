# gallery-dl

> 从多个图床网站下载图片画廊和集合。
> 更多信息：<https://github.com/mikf/gallery-dl>.

- 从指定的 URL 下载图片：

`gallery-dl "{{url}}"`

- 将图片保存到特定的目录：

`gallery-dl --destination {{path/to/directory}} "{{url}}"`

- 从您的网络浏览器中获取已有的 cookies（对于需要登录的网站非常有用）：

`gallery-dl --cookies-from-browser {{browser}} "{{url}}"`

- 获取支持用户名和密码认证的网站上的图片直接 URL：

`gallery-dl --get-urls --username {{username}} --password {{password}} "{{url}}"`

- 通过章节编号和语言筛选漫画章节：

`gallery-dl --chapter-filter "{{10 <= chapter < 20}}" --option "lang={{language_code}}" "{{url}}"`
