# valgrind

> 프로그램의 프로파일링, 최적화 및 디버깅을 위한 전문가용 도구 세트의 래퍼.
> 일반적으로 사용되는 도구로는 `memcheck`, `cachegrind`, `callgrind`, `massif`, `helgrind`, `drd`가 있습니다.
> 더 많은 정보: <https://valgrind.org/docs/manual/manual-core.html#manual-core.options>.

- (기본) Memcheck 도구를 사용하여 `program`의 메모리 사용 진단 표시:

`valgrind {{프로그램}}`

- Memcheck를 사용하여 `program`의 모든 가능한 메모리 누수를 자세히 보고:

`valgrind --leak-check=full --show-leak-kinds=all {{프로그램}}`

- Cachegrind 도구를 사용하여 `program`의 CPU 캐시 작업을 프로파일링하고 기록:

`valgrind --tool=cachegrind {{프로그램}}`

- Massif 도구를 사용하여 `program`의 힙 메모리 및 스택 사용을 프로파일링하고 기록:

`valgrind --tool=massif --stacks=yes {{프로그램}}`
