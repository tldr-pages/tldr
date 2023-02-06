# ld

> Objektumfájlok összekapcsolása. További információ: <https://sourceware.org/binutils/docs-2.38/ld.html>.

- Egy adott, függőségek nélküli objektumfájl összekapcsolása egy végrehajtható fájlba:

`ld {{path/to/file.o}} --output {{path/to/output_executable}}`

- Két objektumfájl összekapcsolása:

`ld {{path/to/file1.o}} {{path/to/file2.o}} --output {{path/to/output_executable}}`

- Egy x86_64 program dinamikus összekapcsolása a glibc-vel (a fájl elérési útvonalak a rendszertől függően változnak):

`ld --output {{path/to/output_executable}} --dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc {{path/to/file.o}} /lib/crtn.o`
