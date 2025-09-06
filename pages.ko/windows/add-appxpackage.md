# Add-AppxPackage

> 서명된 앱 패키지(`.appx`, `.msix`, `.appxbundle`, `.msixbundle`)를 사용자 계정에 추가하는 PowerShell 유틸리티.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/appx/Add-AppxPackage>.

- 앱 패키지 추가:

`Add-AppxPackage -Path {{경로\대상\패키지.msix}}`

- 의존성과 함께 앱 패키지 추가:

`Add-AppxPackage -Path {{경로\대상\패키지.msix}} -DependencyPath {{경로\대상\의존성.msix}}`

- 앱 설치 파일을 사용하여 앱 설치:

`Add-AppxPackage -AppInstallerFile {{경로\대상\앱.appinstaller}}`

- 서명되지 않은 패키지 추가:

`Add-AppxPackage -Path {{경로\대상\패키지.msix}} -DependencyPath {{경로\대상\의존성.msix}} -AllowUnsigned`
