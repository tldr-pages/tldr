# vagrant box

> 管理 Vagrant 盒子（虚拟机镜像）。
> 参见：`vagrant`。
> 更多信息：<https://developer.hashicorp.com/vagrant/docs/cli/box>。

- 列出所有已安装的盒子：

`vagrant box list`

- 添加一个新的盒子：

`vagrant box add {{hashicorp/bionic64}}`

- 从自定义 URL 添加盒子：

`vagrant box add {{my-box}} {{https://example.com/my-box.box}}`

- 移除已安装的盒子：

`vagrant box remove {{hashicorp/bionic64}}`

- 更新当前 Vagrant 环境中使用的所有盒子：

`vagrant box update`

- 更新特定的盒子：

`vagrant box update --box {{bento/debian-12}}`

- 检查当前使用的盒子是否有新版本：

`vagrant box outdated`

- 清理已安装盒子的旧版本：

`vagrant box prune`