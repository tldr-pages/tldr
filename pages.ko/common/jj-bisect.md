# jj bisect

> 이분 탐색을 사용하여 문제가 있는 리비전을 찾음.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-bisect>.

- 테스트 명령을 실행하여 지정한 범위에서 첫 번째 문제 리비전 찾기:

`jj bisect run {{[-r|--range]}} {{정상_리비전}}..{{문제_리비전}} {{명령어}}`

- 쉘 명령을 실행하여 지정한 범위에서 첫 번째 문제 리비전 찾기:

`jj bisect run {{[-r|--range]}} {{정상_리비전}}..{{문제_리비전}} -- bash -c "{{명령어}}"`

- 첫 번째 문제 리비전 대신 첫 번째 정상 리비전 찾기:

`jj bisect run {{[-r|--range]}} {{정상_리비전}}..{{문제_리비전}} --find-good {{명령어}}`

- 파일이 처음 추가된 리비전 찾기:

`jj bisect run {{[-r|--range]}} {{정상_리비전}}..{{문제_리비전}} --find-good -- test -f {{경로/대상/파일}}`
