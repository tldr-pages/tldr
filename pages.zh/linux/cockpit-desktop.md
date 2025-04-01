# cockpit-desktop

> 安全地访问正在运行的会话中的 Cockpit 页面。
> 它在隔离的网络空间中启动 `cockpit-ws` 和一个网页浏览器，并在运行中的用户会话中启动 `cockpit-bridge`。
> 更多信息：<https://cockpit-project.org/guide/latest/cockpit-desktop.1.html>.

- 打开页面：

`cockpit-desktop {{url}} {{SSH_host}}`

- 打开存储页面：

`cockpit-desktop {{/cockpit/@localhost/storage/index.html}}`
