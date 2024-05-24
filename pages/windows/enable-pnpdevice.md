# Enable-PnpDevice

> The Enable-PnpDevice cmdlet enables a Plug and Play (PnP) device. You must use an Administrator account to enable a device.
> This commnand can only be used through Powershell.
> More Information: <https://learn.microsoft.com/powershell/module/pnpdevice/enable-pnpdevice>

- Enable a device:
`Enable-PnpDevice -InstanceId 'RETRIEVED USING Get-PnpDevice COMMAND'`

- Enable all disabled Pnp devices:
`Get-PnpDevice | Where-Object {$_.Problem -eq 22} | Enable-PnpDevice`

- Enable a device without confirmation:
`Enable-PnpDevice -InstanceId 'RETRIEVED USING Get-PnpDevice COMMAND' -Confirm:$False`

- Shows what would happen if the cmdlet runs. The cmdlet is not run:
`Enable-PnpDevice -InstanceId 'USB\VID_5986&;PID_0266&;MI_00\7&;1E5D3568&;0&;0000' -WhatIf:$True`
