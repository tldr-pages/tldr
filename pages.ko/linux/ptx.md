# ptx

> 텍스트 파일에서 단어의 순열 색인을 생성합니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/ptx-invocation.html>.

- 각 줄의 첫 번째 필드가 색인 참조인 순열 색인 생성:

`ptx {{[-r|--references]}} {{경로/대상/파일}}`

- 자동 생성된 색인 참조가 포함된 순열 색인 생성:

`ptx {{[-A|--auto-reference]}} {{경로/대상/파일}}`

- 고정된 너비로 순열 색인 생성:

`ptx {{[-w|--width]}} {{열_너비}} {{경로/대상/파일}}`

- 필터링된 단어 목록으로 순열 색인 생성:

`ptx {{[-o|--only-file]}} {{경로/대상/필터}} {{경로/대상/파일}}`

- SYSV 스타일의 동작으로 순열 색인 생성:

`ptx {{[-G|--traditional]}} {{경로/대상/파일}}`
