# git 发布

> 为发布创建一个 Git 标签。
> 是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-release>。

- 创建并推送一个发布：

`git release {{tag_name}}`

- 创建并推送一个签名发布：

`git release {{tag_name}} -s`

- 创建并推送一个带消息的发布：

`git release {{tag_name}} -m "{{message}}"`