# choco-push

> 将编译好的 NuGet 包 (`nupkg`) 推送到包源。
> 更多信息：<https://docs.chocolatey.org/en-us/create/commands/push>。

- 将编译好的 `nupkg` 推送到指定的包源：

`choco push --source {{https://push.chocolatey.org/}}`

- 将编译好的 `nupkg` 推送到指定的包源，并设置超时时间（默认为 2700 秒）：

`choco push --source {{https://push.chocolatey.org/}} --execution-timeout {{500}}`
