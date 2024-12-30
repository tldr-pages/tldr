# git 重新授权

> 更改作者身份的详细信息。由于此命令会重写 Git 历史，因此下次推送时需要使用 `--force`。
> 属于 `git-extras`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-reauthor>。

- 在整个 Git 仓库中更改作者的邮箱和姓名：

`git reauthor --old-email {{old@example.com}} --correct-email {{new@example.com}} --correct-name "{{name}}"`

- 将邮箱和姓名更改为 Git 配置中定义的：

`git reauthor --old-email {{old@example.com}} --use-config`

- 更改所有提交的邮箱和姓名，无论其原始作者是谁：

`git reauthor --all --correct-email {{name@example.com}} --correct-name {{name}}`