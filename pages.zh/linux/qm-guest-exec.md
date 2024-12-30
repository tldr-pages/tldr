# qm guest exec

> 通过访客代理执行特定命令。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 通过访客代理执行特定命令：

`qm guest exec {{vm_id}} {{command}} {{argument1 argument2 ...}}`

- 通过访客代理异步执行特定命令：

`qm guest exec {{vm_id}} {{argument1 argument2 ...}} --synchronous 0`

- 通过访客代理执行特定命令，并指定10秒的超时时间：

`qm guest exec {{vm_id}} {{argument1 argument2...}} --timeout {{10}}`

- 通过访客代理执行特定命令，并将来自`stdin`的输入转发到访客代理，直到EOF：

`qm guest exec {{vm_id}} {{argument1 argument2 ...}} --pass-stdin 1`