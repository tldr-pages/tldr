# berks

> Chef 菜谱依赖管理器。
> 更多信息：<https://docs.chef.io/berkshelf.html>。

- 安装菜谱依赖到本地仓库：

`berks install`

- 更新特定菜谱及其依赖：

`berks update {{cookbook}}`

- 将菜谱上传到 Chef 服务器：

`berks upload {{cookbook}}`

- 查看菜谱的依赖：

`berks contingent {{cookbook}}`