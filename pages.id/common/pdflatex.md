# pdflatex

> Mengompilasi dokumen PDF dari berkas sumber LaTeX.
> Informasi lebih lanjut: <https://manned.org/pdflatex>.

- Mengompilasi sebuah dokumen PDF:

`pdflatex {{sumber.tex}}`

- Mengompilasi dokumen PDF dengan menentukan direktori keluaran:

`pdflatex -output-directory={{jalan/ke/direktori}} {{sumber.tex}}`

- Mengompilasi dokumen PDF, dan segera berhenti jika terjadi kesalahan (error):

`pdflatex -halt-on-error {{sumber.tex}}`
