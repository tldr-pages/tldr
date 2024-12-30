# packer

> 构建自动化机器镜像。
> 更多信息：<https://www.packer.io/>.

- 构建镜像：

`packer build {{路径/到/配置.json}}`

- 检查 Packer 镜像配置的语法：

`packer validate {{路径/到/配置.json}}`

- 格式化 Packer 镜像配置：

`packer fmt {{路径/到/配置.pkr.hcl}}`