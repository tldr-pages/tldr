# objdump

> 오브젝트 파일에 대한 정보를 표시.
> 더 많은 정보: <https://manned.org/objdump>.

- 파일 헤더 정보를 표시:

`objdump {{[-f|--file-headers]}} {{경로/대상/바이너리}}`

- 모든 헤더 정보를 표시:

`objdump {{[-x|--all-headers]}} {{경로/대상/바이너리}}`

- 실행 가능한 섹션의 디스어셈블리 출력 표시:

`objdump {{[-d|--disassemble]}} {{경로/대상/바이너리}}`

- 인텔 구문으로 실행 가능한 섹션의 디스어셈블리 출력 표시:

`objdump {{[-M|--disassembler-options]}} intel {{[-d|--disassemble]}} {{경로/대상/바이너리}}`

- 모든 섹션의 전체 바이너리 헥스 덤프 표시:

`objdump {{[-s|--full-contents]}} {{경로/대상/바이너리}}`
