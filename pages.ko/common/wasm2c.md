# wasm2c

> WebAssembly 바이너리 형식을 C 소스 파일 및 헤더로 변환.
> 더 많은 정보: <https://github.com/WebAssembly/wabt>.

- 파일을 C 소스 파일 및 헤더로 변환하고 콘솔에 표시:

`wasm2c {{파일.wasm}}`

- 출력 내용을 지정된 파일에 저장 (`file.h`도 추가로 생성됨):

`wasm2c {{파일.wasm}} -o {{파일.c}}`
