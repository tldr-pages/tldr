# gcrane completion

> gcrane에 대한 자동 완성 스크립트를 생성합니다.
> 사용 가능한 쉘은 `bash`, `fish`, `powershell`, 및 `zsh`입니다.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 쉘에 대한 자동 완성 스크립트 생성:

`gcrane completion {{쉘_이름}}`

- 자동 완성 설명 비활성화:

`gcrane completion {{쉘_이름}} --no-descriptions`

- 현재 쉘 세션에 자동 완성 로드 (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- 새 세션에 대한 자동 완성 로드 (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- 도움말 표시:

`gcrane completion {{쉘_이름}} {{[-h|--help]}}`
