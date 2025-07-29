# distcc

> `distccd`와 함께 사용하는 분산 C/C++/ObjC 컴파일 클라이언트입니다.
> 더 많은 정보: <https://manned.org/distcc>.

- `gcc`와 같은 컴파일러로 소스 파일을 컴파일:

`distcc {{gcc}} -c {{path/to/source.c}} -o {{path/to/output.o}}`

- 컴파일을 분산시킬 원격 호스트 설정:

`export DISTCC_HOSTS="localhost {{ip1}} {{ip2}}"`

- `distcc`를 사용해 `make`로 프로젝트를 병렬 컴파일:

`make {{[-j|--jobs]}} {{parallel_jobs}} CC="distcc {{gcc}}"`

- 현재 설정된 `distcc` 호스트 목록 확인:

`distcc --show-hosts`

- 버전 정보 출력:

`distcc --version`

- 도움말 보기:

`distcc --help`
