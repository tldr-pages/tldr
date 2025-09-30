# Remove-AppxPackage

> 사용자 계정에서 앱 패키지를 제거하는 PowerShell 유틸리티입니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/appx/Remove-AppxPackage>.

- 앱 패키지 삭제:

`Remove-AppxPackage {{패키지}}`

- 특정 사용자에 대한 앱 패키지 삭제:

`Remove-AppxPackage {{패키지}} -User {{사용자명}}`

- 모든 사용자에 대한 앱 패키지 삭제:

`Remove-AppxPackage {{패키지}} -AllUsers`

- 앱 패키지를 제거하지만 앱 데이터는 보존:

`Remove-AppxPackage {{패키지}} -PreserveApplicationData`
