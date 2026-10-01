# test

> 파일 유형을 확인하고 값을 비교.
> 조건이 참이면 0, 거짓이면 1을 반환.
> 관련 항목: `[`.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/test-invocation.html>.

- 지정한 변수가 특정 문자열과 같은지 확인:

`test "{{$MY_VAR}}" = "{{/bin/zsh}}"`

- 지정한 변수가 비어있는지 (길이가 0([z]ero)인지) 확인:

`test -z "{{$GIT_BRANCH}}"`

- 지정한 파일([f]ile)이 존재하는지 확인:

`test -f "{{경로/대상/파일}}"`

- 지정한 디렉터리([d]irectory)가 존재하지 않는지 확인:

`test ! -d "{{경로/대상/디렉터리}}"`

- A가 참이면, B를 실행하고, 오류가 발생하면 C 실행 (A가 실패한 경우에도 C가 실행될 수 있음):

`test {{조건}} && {{echo "true"}} || {{echo "false"}}`

- 조건문에서 `test` 사용:

`if test -f "{{경로/대상/파일}}"; then echo "File exists"; else echo "File does not exist"; fi`
