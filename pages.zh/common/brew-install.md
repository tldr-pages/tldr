# brew install

> 安装一个 Homebrew 软件包 (formula)，或安装包 (cask).
> 更多信息：<https://docs.brew.sh/Manpage#install-options-formulacask->.

- 安装软件包/安装包：

`brew install {{软件包|安装包}}`

- 从源码构建，并安装软件包（依赖仍然会以二进制文件的形式安装）：

`brew install {{[-s|--build-from-source]}} {{软件包}}`

- 下载应用清单，输出将要安装的内容（但实际并不会安装任何包）：

`brew install {{[-n|--dry-run]}} {{软件包|安装包}}`
