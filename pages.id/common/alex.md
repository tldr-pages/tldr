# alex

> Alat untuk menangkal karya tulis bahasa Inggris yang ditulis secara tidak sensitif dan berpengertian.
> Alat ini dapat menemukan kata dan frasa bahasa Inggris yang berkaitan kuat dengan gender, polarisasi, ras, agama, dan frasa-frasa sensitif lainnya.
> Informasi lebih lanjut: <https://github.com/get-alex/alex>.

- Analisa teks dari `stdin`:

`echo {{His network looks good}} | alex --stdin`

- Analisa teks dari seluruh file dalam direktori saat ini:

`alex`

- Analisa teks dari suatu file:

`alex {{jalan/menuju/file.md}}`

- Analisa seluruh file Markdown (`.md`) kecuali `contoh.md`:

`alex *.md !{{contoh.md}}`
