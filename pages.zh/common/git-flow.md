# git flow

> 一组 Git 扩展工具，用于提供高级的仓库操作。
> 更多信息：<https://github.com/nvie/gitflow>.

- 在现有的 Git 仓库中初始化：

`git flow init`

- 基于 `develop` 分支开始开发一个特性分支：

`git flow feature start {{feature}}`

- 完成特性分支的开发，将其合并到 `develop` 分支并删除该特性分支：

`git flow feature finish {{feature}}`

- 将特性分支发布到远程服务器：

`git flow feature publish {{feature}}`

- 获取其他用户发布的特性分支：

`git flow feature pull origin {{feature}}`