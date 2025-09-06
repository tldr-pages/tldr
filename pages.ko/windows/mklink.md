# mklink

> 심볼릭 링크를 생성합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/mklink>.

- 파일에 대한 심볼릭 링크 생성:

`mklink {{경로\대상\링크_파일}} {{경로\대상\소스_파일}}`

- 디렉토리에 대한 심볼릭 링크 생성:

`mklink /d {{경로\대상\링크_파일}} {{경로\대상\소스_디렉토리}}`

- 파일에 대한 하드 링크 생성:

`mklink /h {{경로\대상\링크_파일}} {{경로\대상\소스_파일}}`

- 디렉토리 교차점 생성:

`mklink /j {{경로\대상\링크_파일}} {{경로\대상\소스_파일}}`
