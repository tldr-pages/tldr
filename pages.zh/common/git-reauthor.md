# git reauthor

> 更改作者身份的相关信息。由于此命令会重写 Git 历史，下次推送时需要使用 `--force`。
> 作为 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-reauthor>.

- 更改整个 Git 仓库中某个作者的电子邮件和姓名：

`git reauthor --old-email {{old@example.com}} --correct-email {{new@example.com}} --correct-name "{{name}}"`

- 更改电子邮件和姓名为 Git 配置中定义的值：

`git reauthor --old-email {{old@example.com}} --use-config`

- 更改所有提交的电子邮件和姓名，不管原始作者是谁：

`git reauthor --all --correct-email {{name@example.com}} --correct-name {{name}}`
