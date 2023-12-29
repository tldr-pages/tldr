# shuf

> Generate permutasi acak.
> Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1/shuf/>.

- Acak urutan baris di sebuah file dan outputkan hasilnya:

`shuf {{nama_file}}`

- Hanya mengoutputkan 5 entri dari hasil:

`shuf --head-count={{5}} {{nama_file}}`

- Menuliskan output ke file lain:

`shuf {{nama_file}} --output={{nama_file_output}}`

- Men-generate angka acak dari 1-10:

`shuf --input-range={{1-10}}`
