# pacstrap

> Arch Linux 安装脚本，用于将软件包安装到指定的新根目录。
> 更多信息：<https://manned.org/pacstrap.8>.

- 安装 `base` 软件包、Linux 内核和常见硬件的固件：

`pacstrap {{path/to/new/root}} {{base}} {{linux}} {{linux-firmware}}`

- 安装 `base` 软件包、Linux LTS 内核和 `base-devel` 构建工具：

`pacstrap {{path/to/new/root}} {{base}} {{base-devel}} {{linux-lts}}`

- 安装软件包时不将主机的镜像列表复制到目标系统：

`pacstrap -M {{path/to/new/root}} {{packages}}`

- 使用备用的 Pacman 配置文件：

`pacstrap -C {{path/to/pacman.conf}} {{path/to/new/root}} {{packages}}`

- 使用主机上的软件包缓存而不是目标系统上的缓存来安装软件包：

`pacstrap -c {{path/to/new/root}} {{packages}}`

- 在目标系统中初始化一个空的 `pacman` 密钥环而不从主机复制：

`pacstrap -K {{path/to/new/root}} {{packages}}`

- 以交互模式安装软件包（需要确认）：

`pacstrap -i {{path/to/new/root}} {{packages}}`

- 使用软件包文件来安装软件包：

`pacstrap -U {{path/to/new/root}} {{path/to/package1}} {{path/to/package2}}`