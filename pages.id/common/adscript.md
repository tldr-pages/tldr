# adscript

> Penyusun (compiler) untuk file Adscript.
> Informasi lebih lanjut: <https://github.com/Amplus2/Adscript>.

- Susun suatu file menjadi file objek:

`adscript --output {{jalan/menuju/file.o}} {{jalan/menuju/file_input.adscript}}`

- Susun dan gabungkan file menjadi sebuah file program mandiri:

`adscript --executable --output {{jalan/menuju/file}} {{jalan/menuju/file_input.adscript}}`

- Susun sebuah file menggunakan kode LLVM IR daripada kode mesin yang sesungguhnya:

`adscript --llvm-ir --output {{jalan/menuju/file.ll}} {{jalan/menuju/file_input.adscript}}`

- Susun menjadi file objek untuk arsitektur CPU atau sistem operasi yang berbeda dengan mesin saat ini (cross-compile):

`adscript --target-triple {{i386-linux-elf}} --output {{jalan/menuju/file.o}} {{jalan/menuju/file_input.adscript}}`
