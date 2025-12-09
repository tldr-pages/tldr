# wat2wasm

> WebAssembly 텍스트 형식을 바이너리 형식으로 변환.
> 더 많은 정보: <https://webassembly.github.io/wabt/doc/wat2wasm.1.html>.

- 파일을 파싱하고 오류 확인:

`wat2wasm {{파일.wat}}`

- 출력 바이너리를 지정된 파일에 저장:

`wat2wasm {{파일.wat}} -o {{파일.wasm}}`

- 모든 바이트의 단순화된 표현 표시:

`wat2wasm -v {{파일.wat}}`
