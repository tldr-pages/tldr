# 启用-PnpDevice

> Enable-PnpDevice cmdlet 用于启用即插即用 (PnP) 设备。您必须使用管理员帐户才能启用设备。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/pnpdevice/enable-pnpdevice>。

- 启用设备：

`Enable-PnpDevice -InstanceId '使用 Get-PnpDevice 命令检索的值'`

- 启用所有禁用的 PnP 设备：

`Get-PnpDevice | Where-Object {$_.Problem -eq 22} | Enable-PnpDevice`

- 无需确认启用设备：

`Enable-PnpDevice -InstanceId '使用 Get-PnpDevice 命令检索的值' -Confirm:$False`

- 模拟如果 cmdlet 运行时将会发生的情况：

`Enable-PnpDevice -InstanceId 'USB\VID_5986&;PID_0266&;MI_00\7&;1E5D3568&;0&;0000' -WhatIf:$True`