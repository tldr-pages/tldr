# komac

> `winget-pkgs` 저장소용 WinGet 매니페스트 생성 .
> 더 많은 정보: <https://github.com/russellbanks/Komac>.

- 새로운 패키지를 처음부터 생성:

`komac new {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe}}`

- 기존 패키지를 새로운 버전으로 업데이트:

`komac update {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe}}`

- 여러 URL을 사용하여 패키지를 업데이트하고 자동 제출 수행:

`komac update {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe https://example.com/app.msi ...}} {{[-s|--submit]}}`

- winget-pkgs에서 특정 버전 제거:

`komac remove {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}}`

- 패키지의 모든 버전 목록 표시:

`komac {{[list|list-versions]}} {{Package.Identifier}}`

- 자신의 winget-pkgs 포크를 상위 저장소와 동기화:

`komac {{[sync|sync-fork]}}`

- 저장된 GitHub 토큰 추가 또는 업데이트:

`komac token {{[add|update]}} {{[-t|--token]}} {{당신의_Github_토큰}}`

- 쉘 자동완성 스크립트 생성:

`komac {{[complete|autocomplete]}} {{bash|elvish|fish|powershell|zsh}}`
