# Remove-NodeVersion

> `ps-nvm`용 Node.js 런타임 버전 제거.
> 이 명령은 `ps-nvm`의 일부이며 PowerShell에서만 실행할 수 있습니다.
> 더 많은 정보: <https://github.com/aaronpowell/ps-nvm>.

- 특정 Node.js 버전 제거:

`Remove-NodeVersion {{노드_버전}}`

- 여러 Node.js 버전 제거:

`Remove-NodeVersion {{노드_버전1, 노드_버전2, ...}}`

- 현재 설치된 모든 Node.js 20.x 버전 제거:

`Get-NodeVersions -Filter ">=20.0.0 <21.0.0" | Remove-NodeVersion`

- 현재 설치된 모든 Node.js 버전 제거:

`Get-NodeVersions | Remove-NodeVersion`
