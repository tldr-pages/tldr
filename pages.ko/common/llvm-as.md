# llvm-as

> LLVM Intermediate Representation(`.ll`)을 Bitcode(`.bc`)로 변환하는 어셈블러.
> 더 많은 정보: <https://llvm.org/docs/CommandGuide/llvm-as.html>.

- IR 파일을 어셈블:

`llvm-as -o {{경로/대상/출력.bc}} {{경로/대상/소스.ll}}`

- IR 파일을 어셈블하고, 생성된 Bitcode 파일에 모듈 해시 포함:

`llvm-as --module-hash -o {{경로/대상/출력.bc}} {{경로/대상/소스.ll}}`

- `stdin`에서 IR 파일을 읽어 어셈블:

`cat {{경로/대상/소스.ll}} | llvm-as -o {{경로/대상/출력.bc}}`
