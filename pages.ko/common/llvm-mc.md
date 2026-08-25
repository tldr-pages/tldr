# llvm-mc

> LLVM 머신 코드 실험 도구이며, LLVM 머신 코드 작업을 위한 다양한 기능을 제공.
> LLVM의 일부.
> 더 많은 정보: <https://llvm.org/docs/CommandGuide/llvm-mc.html>.

- 어셈블리 코드를 오브젝트 파일 (머신 코드 포함)로 어셈블:

`llvm-mc --filetype=obj -o {{경로/대상/출력_파일.o}} {{경로/대상/입력_파일.s}}`

- 머신 코드가 포함된 오브젝트 파일을 어셈블리 코드로 디스어셈블:

`llvm-mc --disassemble -o {{경로/대상/출력_파일.s}} {{경로/대상/입력_파일.o}}`

- LLVM 비트 코드를 어셈블리 코드로 변환:

`llvm-mc -o {{경로/대상/출력_파일.s}} {{경로/대상/입력_파일.bc}}`

- `stdin`(표준 입력)으로 받은 어셈블리 코드를 어셈블하고 인코딩 결과를 `stdout`(표준 출력)으로 출력:

`echo "{{addl %eax, %ebx}}" | llvm-mc -show-encoding -show-inst`

- `stdin`(표준 입력)으로 받은 머신 코드를 지정한 타겟 아키텍처 기준으로 디스어셈블:

`echo "{{0xCD 0x21}}" | llvm-mc --disassemble -triple={{타겟_이름}}`
