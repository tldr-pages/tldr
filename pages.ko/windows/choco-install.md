# choco install

> Chocolatey를 사용하여 하나 이상의 패키지를 설치합니다.
> 더 많은 정보: <https://chocolatey.org/docs/commands-install>.

- 하나 이상의 패키지 설치:

`choco install {{패키지1 패키지2 ...}}`

- 사용자 지정 구성 파일에서 패키지 설치:

`choco install {{경로\대상\패키지_파일.config}}`

- 특정 `nuspec` 또는 `nupkg` 파일 설치:

`choco install {{경로\대상\파일}}`

- 특정 버전의 패키지 설치:

`choco install {{패키지}} --version {{버전}}`

- 여러 버전의 패키지 설치 허용:

`choco install {{패키지}} --allow-multiple`

- 모든 프롬프트를 자동으로 확인:

`choco install {{패키지}} --yes`

- 패키지를 받을 사용자 지정 소스 지정:

`choco install {{패키지}} --source {{소스_URL|별칭}}`

- 인증을 위한 사용자 명과 비밀번호 제공:

`choco install {{패키지}} --user {{사용자_명}} --password {{비밀번호}}`
