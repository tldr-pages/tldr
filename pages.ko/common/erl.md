# erl

> Erlang 프로그래밍 언어로 프로그램을 실행하고 관리.
> 더 많은 정보: <https://erlang.org/documentation/doc-16.0/erts-16.0/doc/html/erl_cmd.html>.

- 순차적 Erlang 프로그램을 공통 스크립트로 컴파일하고 실행한 후 종료:

`erlc {{경로/대상/파일1 경로/대상/파일2 ...}} && erl -noshell '{{mymodule:myfunction(arguments)}}, init:stop().'`

- 실행중인 Erlang 노드에 연결:

`erl -remsh {{노드이름}}@{{호스트명}} -sname {{커스텀_단축이름}} -hidden -setcookie {{원격노드의_쿠키}}`

- 디렉터리에서 모듈을 로드하도록 Erlang 쉘에 지시:

`erl -pa {{경로/대상/beam파일에_관한_디렉토리}}`
