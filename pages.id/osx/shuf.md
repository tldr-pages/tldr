# shuf

> Generate permutasi acak.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/shuf>.

- Acak urutan baris di sebuah file dan outputkan hasilnya:

`shuf {{nama_file}}`

- Hanya mengoutputkan 5 entri dari hasil:

`shuf -n {{5}} {{nama_file}}`

- Menuliskan output ke file lain:

`shuf {{nama_file}} -o {{nama_file_output}}`

- Men-generate angka acak dari 1-10:

`shuf -i {{1-10}}`
