# ld

> 오브젝트 파일을 함께 링크.
> 더 많은 정보: <https://sourceware.org/binutils/docs/ld.html>.

- 특정 오브젝트 파일을 의존성 없이 실행 파일로 링크:

`ld {{경로/대상/파일.o}} --output {{경로/대상/출력_실행파일}}`

- 두 오브젝트 파일을 함께 링크:

`ld {{경로/대상/파일1.o}} {{경로/대상/파일2.o}} --output {{경로/대상/출력_실행파일}}`

- x86_64 프로그램을 glibc에 동적으로 링크 (파일 경로는 시스템에 따라 달라짐):

`ld --output {{경로/대상/출력_실행파일}} --dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc {{경로/대상/파일.o}} /lib/crtn.o`
