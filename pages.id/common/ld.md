# ld

> Hubungkan berkas-berkas obyek berbarengan untuk membangun suatu berkas program executable.
> Informasi lebih lanjut: <https://sourceware.org/binutils/docs/ld.html>.

- Hubungkan berkas obyek tertentu yang tidak memiliki kebergantungan ke suatu executable:

`ld {{jalan/menuju/berkas.o}} {{[-o|--output]}} {{jalan/menuju/output_executable}}`

- Hubungkan dua berkas obyek berbarengan:

`ld {{jalan/menuju/berkas1.o}} {{jalan/menuju/berkas2.o}} {{[-o|--output]}} {{jalan/menuju/output_executable}}`

- Hubungkan secara dinamis sebuah program x86_64 ke glibc (jalan-jalan berkas berubah bergantung pada sistem):

`ld {{[-o|--output]}} {{jalan/menuju/output_executable}} {{[-I|--dynamic-linker]}} /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc {{jalan/menuju/berkas.o}} /lib/crtn.o`
