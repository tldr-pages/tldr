# llvm-dis

> LLVM 비트코드 파일을 사람이 읽을 수 있는 LLVM 중간 표현(IR)로 변환.
> 더 많은 정보: <https://www.llvm.org/docs/CommandGuide/llvm-dis.html>.

- 비트코드 파일을 LLVM IR로 변환하고 결과를 `stdout`으로 출력:

`llvm-dis {{경로/대상/입력.bc}} -o -`

- 비트코드 파일을 동일한 파일 이름의 LLVM IR 파일로 변환:

`llvm-dis {{경로/대상/파일.bc}}`

- 비트코드 파일을 LLVM IR로 변환하고 결과를 지정된 파일에 기록:

`llvm-dis {{경로/대상/입력.bc}} -o {{경로/대상/출력.ll}}`
