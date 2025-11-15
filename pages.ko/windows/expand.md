# expand

> Windows Cabinet 파일 압축 해제.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/expand>.

- 단일 파일 Cabinet 파일을 지정한 디렉토리로 압축 해제:

`expand {{경로\대상\파일.cab}} {{경로\대상\디렉토리}}`

- 소스 Cabinet 파일 내 파일 목록 표시:

`expand {{경로\대상\파일.cab}} {{경로\대상\디렉토리}} -d`

- Cabinet 파일의 모든 파일 압축 해제:

`expand {{경로\대상\파일.cab}} {{경로\대상\디렉토리}} -f:*`

- Cabinet 파일에서 특정 파일 압축 해제:

`expand {{경로\대상\파일.cab}} {{경로\대상\디렉토리}} -f:{{경로\대상\파일}}`

- 압축 해제 시 디렉토리 구조를 무시하고 단일 디렉토리에 추가:

`expand {{경로\대상\파일.cab}} {{경로\대상\디렉토리}} -i`
