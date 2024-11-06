# Set-NodeVersion

> `ps-nvm`에서 기본 Node.js 버전을 설정.
> `ps-nvm`의 일부이며 PowerShell에서만 실행 가능.
> 더 많은 정보: <https://github.com/aaronpowell/ps-nvm>.

- 현재 PowerShell 세션에서 특정 버전의 Node.js 사용:

`Set-NodeVersion {{node_버전}}`

- 최신 설치된 Node.js 버전 20.x 사용:

`Set-NodeVersion ^20`

- 현재 사용자에 대해 기본 Node.js 버전 설정 (향후 PowerShell 세션에만 적용됨):

`Set-NodeVersion {{node_버전}} -Persist User`

- 모든 사용자를 위해 기본 Node.js 버전 설정 (관리자/루트 권한으로 실행해야 하며 향후 PowerShell 세션에만 적용됨):

`Set-NodeVersion {{node_버전}} -Persist Machine`
