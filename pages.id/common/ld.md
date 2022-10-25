# ld

> Menghubungkan file-file obyek berbarengan.
> Informasi lebih lanjut: <https://sourceware.org/binutils/docs-2.38/ld.html>.

- Menghubungkan file obyek tertentu yang tidak memiliki kebergantungan ke suatu executable:

`ld {{jalan/menuju/file.o}} --output {{jalan/menuju/output_executable}}`

- Menghubungkan 2 file obyek berbarengan:

`ld {{jalan/menuju/file1.o}} {{jalan/menuju/file2.o}} --output {{jalan/menuju/output_executable}}`

- Menghubungkan secara dinamis sebuah program x86_64 ke glibc (jalan-jalan file berubah bergantung pada sistem):

`ld --output {{jalan/menuju/output_executable}} --dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc {{jalan/menuju/file.o}} /lib/crtn.o`
