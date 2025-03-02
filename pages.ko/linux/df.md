# df

> 파일 시스템 디스크 공간 사용 개요를 표시합니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>.

- 모든 파일 시스템과 디스크 사용량 표시:

`df`

- 모든 파일 시스템과 디스크 사용량을 사람이 읽기 쉬운 형식으로 표시:

`df {{[-h|--human-readable]}}`

- 주어진 파일 또는 디렉토리를 포함하는 파일 시스템과 디스크 사용량 표시:

`df {{경로/대상/파일_또는_폴더}}`

- 사용 가능한 inode 수에 대한 통계 포함:

`df {{[-i|--inodes]}}`

- 특정 유형을 제외한 파일 시스템 표시:

`df {{[-x|--exclude-type]}} {{squashfs}} {{[-x|--exclude-type]}} {{tmpfs}}`

- 파일 시스템 유형 표시:

`df {{[-T|--print-type]}}`
