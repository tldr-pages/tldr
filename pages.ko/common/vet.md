# vet

> 패키지 manifest, 디렉터리, 컨테이너 이미지 또는 GitHub 저장소를 검사해 취약점과 악성 패키지를 탐지하고, CEL 표현식으로 보안 정책을 적용.
> 더 많은 정보: <https://safedep.github.io/vet/vet.html>.

- 현재 디렉터리 검사:

`vet scan {{[-D|--directory]}} .`

- `package-lock.json` manifest 파일 검사:

`vet scan {{[-M|--manifests]}} {{경로/대상/manifest_파일}}`

- 코드베이스에서 심각도 critical의 취약점이 하나라도 발견되면, 실패하도록 필터를 적용해 검사:

`vet scan {{[-D|--directory]}} {{경로/대상/디렉터리}} --filter 'vulns.critical.exists(p, true)' --filter-fail`

- 지정한 오픈 소스 소프트웨어 패키지 악성 코드 검사:

`vet inspect malware --purl {{패키지_주소}}`

- Cursor 등의 코드 편집기에서 AI 기반 보안 기능을 사용할 수 있도록 MCP 서버 시작:

`vet server mcp`
