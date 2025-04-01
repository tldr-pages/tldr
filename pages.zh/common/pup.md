# pup

> 命令行 HTML 解析工具。
> 更多信息：<https://github.com/ericchiang/pup>。

- 将原始 HTML 文件转换为干净、缩进和着色的格式：

`cat {{index.html}} | pup --color`

- 按元素标签名称过滤 HTML：

`cat {{index.html}} | pup '{{tag}}'`

- 按 ID 过滤 HTML：

`cat {{index.html}} | pup '{{div#id}}'`

- 按属性值过滤 HTML：

`cat {{index.html}} | pup '{{input[type="text"]}}'`

- 打印过滤后的 HTML 元素及其子元素的所有文本：

`cat {{index.html}} | pup '{{div}} text{}'`

- 以 JSON 格式打印 HTML：

`cat {{index.html}} | pup '{{div}} json{}'`