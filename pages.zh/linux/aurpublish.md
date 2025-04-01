# aurpublish

> 发布 Arch 用户仓库的软件包。
> 更多信息：<https://github.com/eli-schwartz/aurpublish>。

- 验证 `PKGBUILD` 的完整性，生成 `.SRCINFO`，创建提交信息模板，并将软件包发布到 AUR：

`aurpublish {{package_name}}`

- 为当前仓库添加 Git 钩子：

`aurpublish setup`

- 显示帮助：

`aurpublish {{[-h|--help]}}`
