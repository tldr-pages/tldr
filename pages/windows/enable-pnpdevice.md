# Enable-PnpDevice

> Enable a Plug and Play (PnP) device. You must use an Administrator account to enable a device.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/pnpdevice/enable-pnpdevice>.

- Enable a device:

`Enable-PnpDevice -InstanceId 'RETRIEVED USING Get-PnpDevice COMMAND'`

- Enable all disabled PnP devices:

`Get-PnpDevice | Where-Object {$_.Problem -eq 22} | Enable-PnpDevice`

- Enable a device without confirmation:

`Enable-PnpDevice -InstanceId 'RETRIEVED USING Get-PnpDevice COMMAND' -Confirm:$False`

- Simulate what would happen if the cmdlet runs:

`Enable-PnpDevice -InstanceId 'USB\VID_5986&;PID_0266&;MI_00\7&;1E5D3568&;0&;0000' -WhatIf:$True`
