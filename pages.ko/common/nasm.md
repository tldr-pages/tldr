# nasm

> Netwide Assembler, 휴대용 80x86 어셈블러.
> 더 많은 정보: <https://www.nasm.us/xdoc/2.16.03/html/nasmdoc2.html>.

- `source.asm`을 (기본) raw 바이너리 형식의 바이너리 파일 `source`로 어셈블:

`nasm {{source.asm}}`

- `source.asm`을 지정된 형식의 바이너리 파일 `output_file`로 어셈블:

`nasm -f {{형식}} {{source.asm}} -o {{출력_파일}}`

- 유효한 출력 형식 목록 나열(기본 nasm 도움말 포함):

`nasm -hf`

- 어셈블하고 어셈블리 목록 파일 생성:

`nasm -l {{목록_파일}} {{source.asm}}`

- 어셈블하기 전에 포함 파일 검색 경로에 디렉토리 추가(마지막에 슬래시 포함 필요):

`nasm -i {{경로/대상/포함_폴더/}} {{source.asm}}`
