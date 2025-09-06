# adscript

> Adscript 파일용 컴파일러.
> 더 많은 정보: <https://github.com/Amplus2/Adscript>.

- 파일을 객체 파일로 컴파일:

`adscript --output {{경로/대상/파일.o}} {{경로/대상/입력_파일.adscript}}`

- 파일을 컴파일하고 독립 실행형 실행 파일에 연결:

`adscript --executable --output {{경로/대상/파일}} {{경로/대상/입력_파일.adscript}}`

- 기본 기계어 코드 대신 LLVM IR로 파일 컴파일:

`adscript --llvm-ir --output {{경로/대상/파일.ll}} {{경로/대상/입력_파일.adscript}}`

- 파일을 외부 CPU 아키텍처 또는 운영 체제용 객체 파일로 크로스 컴파일:

`adscript --target-triple {{i386-linux-elf}} --output {{경로/대상/파일.o}} {{경로/대상/입력_파일.adscript}}`
