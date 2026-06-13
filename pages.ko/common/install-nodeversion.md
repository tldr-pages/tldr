# Install-NodeVersion

> `ps-nvm`에 대한 Node.js 런타임 버전 설치.
> 이 명령어는 `ps-nvm`의 일부이며 PowerShell에서만 실행할 수 있습니다.
> 더 많은 정보: <https://github.com/aaronpowell/ps-nvm>.

- 특정 Node.js 버전 설치:

`Install-NodeVersion {{노드_버전}}`

- 여러 개의 Node.js 버전 설치:

`Install-NodeVersion {{노드_버전1, 노드_버전2, ...}}`

- 최신 사용 가능한 Node.js 20 버전 설치:

`Install-NodeVersion ^20`

- x86 (x86 32-bit) / x64 (x86 64-bit) / arm64 (ARM 64-bit) 버전의 Node.js 설치:

`Install-NodeVersion {{노드_버전}} -Architecture {{x86|x64|arm64}}`

- HTTP 프록시를 사용하여 Node.js 다운로드:

`Install-NodeVersion {{노드_버전}} -Proxy {{http://example.com}}`
