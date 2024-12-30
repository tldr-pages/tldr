# 设置节点安装位置

> 为 `ps-nvm` 设置默认的 Node.js 安装目录。
> 该命令是 `ps-nvm` 的一部分，仅能在 PowerShell 下运行。
> 更多信息：<https://github.com/aaronpowell/ps-nvm>。

- 将 Node.js 安装位置更改为指定目录（`ps-nvm` 将创建一个新的 `.nvm` 子目录来安装它们）：

`Set-NodeInstallLocation {{path/to/directory}}`