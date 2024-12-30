# cowsay

> 打印ASCII艺术（默认是牛）说或想某些事情。
> 更多信息：<https://github.com/tnalpgge/rank-amateur-cowsay>。

- 打印一只ASCII牛说“你好，世界”：

`cowsay "{{你好，世界}}"`

- 打印一只ASCII牛说来自`stdin`的文本：

`echo "{{你好，世界}}" | cowsay`

- 列出所有可用的艺术类型：

`cowsay -l`

- 打印指定的ASCII艺术说“你好，世界”：

`cowsay -f {{艺术}} "{{你好，世界}}"`

- 打印一只死去的思考中的ASCII牛：

`cowthink -d "{{我只是一头牛，不是伟大的思想家...}}"`

- 打印一只带有自定义眼睛的ASCII牛说“你好，世界”：

`cowsay -e {{字符}} "{{你好，世界}}"`