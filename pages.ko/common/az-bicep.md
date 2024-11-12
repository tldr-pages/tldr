# az bicep

> Bicep CLI 명령어 집합.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/bicep>.

- Bicep CLI 설치:

`az bicep install`

- Bicep 파일 빌드:

`az bicep build --file {{경로/대상/파일.bicep}}`

- ARM 템플릿 파일을 Bicep 파일로 디컴파일 하려고 시도:

`az bicep decompile --file {{경로/대상/템플릿_파일.json}}`

- Bicep CLI를 최신 버전으로 업그레이드:

`az bicep upgrade`

- 설치된 Bicep CLI 버전을 표시:

`az bicep version`

- 사용 가능한 모든 Bicep CLI 버전 나열:

`az bicep list-versions`

- Bicep CLI 설치 삭제:

`az bicep uninstall`
