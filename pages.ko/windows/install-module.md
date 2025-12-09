# Install-Module

> PowerShell Gallery, NuGet 및 기타 리포지토리에서 PowerShell 모듈을 설치합니다.
> 더 많은 정보: <https://learn.microsoft.com/powershell/module/powershellget/install-module>.

- 모듈 설치 또는 최신 버전으로 업데이트:

`Install-Module {{모듈}}`

- 특정 버전의 모듈 설치:

`Install-Module {{모듈}} -RequiredVersion {{버전}}`

- 최소 버전을 사용하여 모듈 설치:

`Install-Module {{모듈}} -MinimumVersion {{버전}}`

- 모듈의 지원되는 버전 범위를 지정하여 설치:

`Install-Module {{모듈}} -MinimumVersion {{최소_버전}} -MaximumVersion {{최대_버전}}`

- 특정 리포지토리에 모듈 설치:

`Install-Module {{모듈}} -Repository {{리포지토리}}`

- 지정된 리포지토리들에서 모듈 설치:

`Install-Module {{모듈}} -Repository {{리포지토리1, 리포지토리2, ...}}`

- 모듈을 모든 사용자 또는 현재 사용자에게 설치:

`Install-Module {{모듈}} -Scope {{AllUsers|CurrentUser}}`

- `Install-Module`을 통해 설치, 업그레이드 또는 제거될 모듈을 확인하기 위한 테스트 실행:

`Install-Module {{모듈}} -WhatIf`
