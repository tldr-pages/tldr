# pkgctl repo

> 管理 Arch Linux 的 Git 打包仓库及其配置。
> 另请参见：`pkgctl`。
> 更多信息：<https://manned.org/pkgctl-repo.1>。

- 克隆一个软件包仓库（需要在你的 Arch Linux GitLab 帐户中设置 SSH 密钥）：

`pkgctl repo clone {{pkgname}}`

- 通过 HTTPS 克隆一个软件包仓库：

`pkgctl repo clone --protocol=https {{pkgname}}`

- 创建一个新的 GitLab 软件包仓库并在创建后克隆它（需要有效的 GitLab API 认证）：

`pkgctl repo create {{pkgbase}}`

- 将软件包仓库切换到指定版本：

`pkgctl repo switch {{version}} {{pkgbase}}`

- 打开软件包仓库的网站：

`pkgctl repo web {{pkgbase}}`