# test

> 파일 유형을 확인하고 값을 비교.
> 조건이 참이면 0을 반환하고, 거짓이면 1을 반환합니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/test-invocation.html>.

- 주어진 변수가 특정 문자열과 같은지 확인:

`test "{{$MY_VAR}}" = "{{/bin/zsh}}"`

- 주어진 변수가 비어 있는지 확인:

`test -z "{{$GIT_BRANCH}}"`

- 파일이 존재하는지 확인:

`test -f "{{경로/대상/파일_또는_폴더}}"`

- 디렉토리가 존재하지 않는지 확인:

`test ! -d "{{경로/대상/폴더}}"`

- A가 참이면 B를 실행하고, 오류가 발생하면 C를 실행 (A가 실패해도 C가 실행될 수 있음):

`test {{조건}} && {{echo "true"}} || {{echo "false"}}`
