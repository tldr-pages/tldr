# yadm clone

> 功能就像 `git clone`。此外，你还可以传递额外的标志来配置你的仓库。
> 如果仓库中有一个引导文件，将提示你执行它。
> 请参阅：`git clone`。
> 更多信息：<https://yadm.io/docs/common_commands>.

- 克隆一个已有的仓库：

`yadm clone {{远程_仓库_位置}}`

- 克隆一个已有的仓库，然后执行引导文件：

`yadm clone {{远程_仓库_位置}} --bootstrap`

- 克隆一个已有的仓库，并在克隆后不执行引导文件：

`yadm clone {{远程_仓库_位置}} --no-bootstrap`

- 更改 `yadm` 在克隆时使用的工作树：

`yadm clone {{远程_仓库_位置}} --w {{工作树_文件}}`

- 更改 `yadm` 用于获取文件的分支：

`yadm clone {{远程_仓库_位置}} -b {{分支}}`

- 覆盖一个已有仓库的本地分支：

`yadm clone {{远程_仓库_位置}} -f`
