# ip route list

> 用於顯示 IP 路由表管理的子指令.
> 更多資訊：<https://manned.org/ip-route>.

- 顯示 `main` 路由表：

`ip {{[r|route]}} {{[l|list]}}`

- 顯示主要路由表（與第一個範例相同）：

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{main|254}}`

- 顯示 local（本機）路由表：

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{local|255}}`

- 顯示所有路由表：

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{all|unspec|0}}`

- 僅列出指定網路介面的路由：

`ip {{[r|route]}} {{[l|list]}} dev {{ethX}}`

- 列出指定 scope（作用範圍）的路由：

`ip {{[r|route]}} {{[l|list]}} {{[s|scope]}} link`

- 顯示 routing cache（路由快取）：

`ip {{[r|route]}} {{[l|list]}} {{[c|cache]}}`

- 僅顯示 IPv6 或 IPv4 路由：

`ip {{-6|-4}} {{[r|route]}}`
