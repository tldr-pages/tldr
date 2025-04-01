# git notes

> 添加或查看对象注释。
> 更多信息：<https://git-scm.com/docs/git-notes>。

- 列出所有注释及其附带的对象：

`git notes list`

- 列出特定对象（默认为 HEAD）上附带的所有注释：

`git notes list [{{object}}]`

- 显示特定对象（默认为 HEAD）上附带的注释：

`git notes show [{{object}}]`

- 向指定对象追加注释（打开默认文本编辑器）：

`git notes append {{object}}`

- 向指定对象追加注释，并指定消息内容：

`git notes append --message="{{message_text}}"`

- 编辑现有注释（默认为 HEAD）：

`git notes edit [{{object}}]`

- 从一个对象复制注释到另一个对象：

`git notes copy {{source_object}} {{target_object}}`

- 删除指定对象上添加的所有注释：

`git notes remove {{object}}`