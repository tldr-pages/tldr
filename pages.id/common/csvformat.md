# csvformat

> Ubah sebuah file CSV ke dalam format keluaran (output) kustom.
> Bagian dari csvkit.
> Informasi lebih lanjut: <https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>.

- Ubah menjadi berkas yang dipisahkan oleh tab (TSV):

`csvformat {{[-T|--out-tabs]}} {{data.csv}}`

- Ubah pembatas (delimiter) menjadi karakter kustom:

`csvformat {{[-D|--out-delimiter]}} "{{karakter_pembatas}}" {{data.csv}}`

- Ubah akhiran baris menjadi carriage return (^M) + line feed:

`csvformat {{[-M|--out-lineterminator]}} "{{\r\n}}" {{data.csv}}`

- Minimalkan penggunaan karakter tanda kutip:

`csvformat {{[-U|--out-quoting]}} 0 {{data.csv}}`

- Maksimalkan penggunaan karakter tanda kutip:

`csvformat {{[-U|--out-quoting]}} 1 {{data.csv}}`
