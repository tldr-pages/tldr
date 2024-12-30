# yadm-clone

> 与 `git clone` 的功能相同。此外，您可以传递额外的标志以配置您的存储库。
> 如果存储库中有引导文件，系统会提示您执行它。
> 另请参阅：`git clone`。
> 更多信息：<https://yadm.io/docs/common_commands>。

- 克隆一个现有的存储库：

`yadm clone {{remote_repository_location}}`

- 克隆一个现有的存储库，然后执行引导文件：

`yadm clone {{remote_repository_location}} --bootstrap`

- 克隆一个现有的存储库，并在克隆后不执行引导文件：

`yadm clone {{remote_repository_location}} --no-bootstrap`

- 更改 `yadm` 在克隆过程中将使用的工作树：

`yadm clone {{remote_repository_location}} --w {{worktree_file}}`

- 更改 `yadm` 获取文件的分支：

`yadm clone {{remote_repository_location}} -b {{branch}}`

- 覆盖现有存储库的本地分支：

`yadm clone {{remote_repository_location}} -f`