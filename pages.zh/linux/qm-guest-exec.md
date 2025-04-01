# qm guest exec

> 通过来宾代理执行特定命令。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 通过来宾代理执行特定命令：

`qm guest exec {{vm_id}} {{command}} {{argument1 argument2 ...}}`

- 通过来宾代理异步执行特定命令：

`qm guest exec {{vm_id}} {{argument1 argument2 ...}} --synchronous 0`

- 通过来宾代理执行特定命令，并设置10秒的超时时间：

`qm guest exec {{vm_id}} {{argument1 argument2...}} --timeout {{10}}`

- 通过来宾代理执行特定命令，并将 `stdin` 中的内容转发到来宾代理，直到遇到 EOF：

`qm guest exec {{vm_id}} {{argument1 argument2 ...}} --pass-stdin 1`
