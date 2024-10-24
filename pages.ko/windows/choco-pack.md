# choco pack

> NuGet 사양을 `nupkg` 파일로 패키징.
> 더 많은 정보: <https://chocolatey.org/docs/commands-pack>.

- NuGet 사양을 `nupkg` 파일로 패키징:

`choco pack {{경로\대상\사양_파일}}`

- 결과 파일의 버전을 지정하여 NuGet 사양 패키징:

`choco pack {{경로\대상\사양_파일}} --version {{버전}}`

- 특정 디렉토리에 NuGet 사양 패키징:

`choco pack {{경로\대상\사양_파일}} --output-directory {{경로\대상\출력_디렉토리}}`
