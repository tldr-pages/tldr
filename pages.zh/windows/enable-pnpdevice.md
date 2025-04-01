# Enable-PnpDevice

> 启用 Plug and Play (PnP) 设备的 cmdlet。必须使用管理员账户才能启用设备。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/pnpdevice/enable-pnpdevice>.

- 启用一个设备：

`Enable-PnpDevice -InstanceId '使用 Get-PnpDevice 命令获取'`

- 启用所有已禁用的 PnP 设备：

`Get-PnpDevice | Where-Object {$_.Problem -eq 22} | Enable-PnpDevice`

- 不需要确认直接启用设备：

`Enable-PnpDevice -InstanceId '使用 Get-PnpDevice 命令获取' -Confirm:$False`

- 干运行，显示如果 cmdlet 运行会发生什么：

`Enable-PnpDevice -InstanceId 'USB\VID_5986&PID_0266&MI_00\7&1E5D3568&0&0000' -WhatIf:$True`
