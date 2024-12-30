# git 注释

> 添加或检查对象注释。
> 更多信息：<https://git-scm.com/docs/git-notes>。

- 列出所有注释及其附加的对象：

`git notes list`

- 列出附加到指定对象的所有注释（默认为 HEAD）：

`git notes list [{{对象}}]`

- 显示附加到指定对象的注释（默认为 HEAD）：

`git notes show [{{对象}}]`

- 将注释附加到指定对象（打开默认文本编辑器）：

`git notes append {{对象}}`

- 将注释附加到指定对象，并指定消息：

`git notes append --message="{{消息文本}}"`

- 编辑现有注释（默认为 HEAD）：

`git notes edit [{{对象}}]`

- 从一个对象复制注释到另一个对象：

`git notes copy {{源对象}} {{目标对象}}`

- 移除附加到指定对象的所有注释：

`git notes remove {{对象}}`