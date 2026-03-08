# pdftex

> Mengompilasi dokumen PDF dari berkas sumber TeX.
> Informasi lebih lanjut: <https://www.tug.org/applications/pdftex/>.

- Mengompilasi sebuah dokumen PDF:

`pdftex {{sumber.tex}}`

- Mengompilasi dokumen PDF dengan menentukan direktori keluaran:

`pdftex -output-directory={{jalan/ke/direktori}} {{sumber.tex}}`

- Mengompilasi dokumen PDF, dan segera berhenti jika terjadi kesalahan (error):

`pdftex -halt-on-error {{sumber.tex}}`
