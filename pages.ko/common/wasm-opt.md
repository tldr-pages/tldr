# wasm-opt

> WebAssembly 바이너리 파일 최적화.
> 더 많은 정보: <https://manned.org/wasm-opt>.

- 기본 최적화를 적용하고 지정된 파일에 저장:

`wasm-opt -O {{입력.wasm}} -o {{출력.wasm}}`

- 모든 최적화를 적용하고 지정된 파일에 저장 (시간이 더 걸리지만 최적의 코드를 생성):

`wasm-opt -O4 {{입력.wasm}} -o {{출력.wasm}}`

- 파일을 크기 위주로 최적화:

`wasm-opt -Oz {{입력.wasm}} -o {{출력.wasm}}`

- 바이너리의 텍스트 표현을 콘솔에 출력:

`wasm-opt {{입력.wasm}} --print`
