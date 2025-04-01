# podman login

> 登录到容器镜像仓库。
> 注意：在 Linux 上，默认的认证文件路径是 `$XDG_RUNTIME_DIR/containers/auth.json`，通常存储在 `tmpfs`（内存中）。
> 更多信息：<https://docs.podman.io/en/latest/markdown/podman-login.1.html>。

- 登录到仓库（在 Linux 上非持久化；在 Windows/macOS 上持久化）：

`podman login {{registry.example.org}}`

- 在 Linux 上持久化登录到仓库：

`podman login --authfile $HOME/.config/containers/auth.json {{registry.example.org}}`

- 登录到不安全（HTTP）的仓库：

`podman login --tls-verify=false {{registry.example.org}}`
