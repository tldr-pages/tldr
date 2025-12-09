# bison

> GNU 파서 생성기.
> 더 많은 정보: <https://manned.org/bison>.

- bison 정의 파일을 컴파일:

`bison {{경로/대상/file.y}}`

- 디버그 모드에서 컴파일하면, 결과 파서가 `stdout`에 추가 정보를 쓰게 됨:

`bison --debug {{경로/대상/file.y}}`

- 출력 파일 이름 지정:

`bison --output {{경로/대상/output.c}} {{경로/대상/file.y}}`

- 컴파일할 때 세세한 정보를 같이 출력:

`bison --verbose`
