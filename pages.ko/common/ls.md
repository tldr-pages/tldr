# ls

> 폴더의 내용물을 리스팅합니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- 한줄에 하나의 파일씩 나열:

`ls -1`

- 숨겨진 파일을 포함해 모든 파일 나열:

`ls {{[-a|--all]}}`

- 모든 파일 나열, 폴더명에는 뒤에 '/'를 붙음:

`ls {{[-F|--classify]}}`

- 파일의 모든 정보(권한, 소유자, 크기, 그리고 수정날짜)를 나열:

`ls {{[-la|--all -l]}}`

- 파일의 모든정보를 나열, 다만 크기는 읽기쉽게 (KiB, MiB, GiB)를 사용:

`ls {{[-lh|-l --human-readable]}}`

- 파일의 모든 정보를 크기의 내림차순으로 정렬:

`ls {{-lSR|-lS --recursive}}`

- 파일의 모든 정보를 수정날짜(오래된 순서)로 정렬:

`ls {{[-ltr|-lt --reverse]}}`

- 폴더만 나열:

`ls {{[-d|--directory]}} */`
