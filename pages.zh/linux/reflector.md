# reflector

> 用于获取并排序 Arch Linux 镜像列表的脚本。
> 更多信息：<https://manned.org/reflector>.

- 获取所有镜像，按下载速度排序并保存：

`sudo reflector --sort {{rate}} --save {{/etc/pacman.d/mirrorlist}}`

- 仅获取德国的 HTTPS 镜像：

`reflector --country {{Germany}} --protocol {{https}}`

- 仅获取最近同步的 10 个镜像：

`reflector --latest {{10}}`

- 使用配置文件获取镜像：

`sudo reflector @{{/etc/xdg/reflector/reflector.conf}}`

- 显示帮助：

`reflector {{[-h|--help]}}`