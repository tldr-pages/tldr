# Enable-PnpDevice

> Enable-PnpDevice cmdlet은 플러그 앤 플레이(PnP) 장치를 활성화합니다. 장치를 활성화하려면 관리자 계정을 사용해야 합니다.
> 참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/pnpdevice/enable-pnpdevice>.

- 장치 활성화:

`Enable-PnpDevice -InstanceId 'Get-PnpDevice 명령을 통해 검색된 값'`

- 비활성화된 모든 PnP 장치 활성화:

`Get-PnpDevice | Where-Object {$_.Problem -eq 22} | Enable-PnpDevice`

- 확인 없이 장치 활성화:

`Enable-PnpDevice -InstanceId 'Get-PnpDevice 명령을 통해 검색된 값' -Confirm:$False`

- cmdlet 실행 시의 결과를 예측:

`Enable-PnpDevice -InstanceId 'USB\VID_5986&;PID_0266&;MI_00\7&;1E5D3568&;0&;0000' -WhatIf:$True`
