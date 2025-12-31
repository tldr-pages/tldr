# shred

> 파일을 덮어써서 데이터를 안전하게 삭제.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html>.

- 파일 덮어쓰기:

`shred {{경로/대상/파일}}`

- 파일을 덮어쓰고 진행 상황 표시:

`shred --verbose {{경로/대상/파일}}`

- 파일을 덮어쓰고 무작위 데이터 대신 [z]ero(0)로 남기기:

`shred --zero {{경로/대상/파일}}`

- 파일을 특정 횟수[n]만큼 덮어쓰기:

`shred --iterations {{25}} {{경로/대상/파일}}`

- 파일을 덮어쓰고 삭제:

`shred --remove {{경로/대상/파일}}`

- 파일을 100번 덮어쓰고 마지막에 [z]ero(0)로 덮어쓰기 추가, 덮어쓰기 후 파일 삭제 및 진행 상황을 화면에 [v]자세히 표시:

`shred -vzun 100 {{경로/대상/파일}}`
