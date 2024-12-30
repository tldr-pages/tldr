# berks

> Chef 厨房书依赖管理器。
> 更多信息： <https://docs.chef.io/berkshelf.html>。

- 将厨房书依赖项安装到本地仓库：

`berks install`

- 更新特定的厨房书及其依赖项：

`berks update {{cookbook}}`

- 将厨房书上传到 Chef 服务器：

`berks upload {{cookbook}}`

- 查看厨房书的依赖项：

`berks contingent {{cookbook}}`