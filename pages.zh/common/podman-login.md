# podman 登录

> 登录到容器注册中心。
> 注意：在 Linux 上，默认的认证文件路径是 `$XDG_RUNTIME_DIR/containers/auth.json`，通常存储在 `tmpfs`（内存中）。
> 更多信息：<https://docs.podman.io/en/latest/markdown/podman-login.1.html>。

- 登录到注册中心（在 Linux 上为非持久性；在 Windows/macOS 上为持久性）：

`podman login {{registry.example.org}}`

- 在 Linux 上持久性地登录到注册中心：

`podman login --authfile $HOME/.config/containers/auth.json {{registry.example.org}}`

- 登录到不安全的（HTTP）注册中心：

`podman login --tls-verify=false {{registry.example.org}}`