# choco-push

> 将已编译的 NuGet 包（`nupkg`）推送到包源。
> 更多信息：<https://docs.chocolatey.org/en-us/create/commands/push>。

- 将已编译的 `nupkg` 推送到指定的源：

`choco push --source {{https://push.chocolatey.org/}}`

- 将已编译的 `nupkg` 推送到指定的源，并设置超时时间（单位：秒，默认值为 2700）：

`choco push --source {{https://push.chocolatey.org/}} --execution-timeout {{500}}`