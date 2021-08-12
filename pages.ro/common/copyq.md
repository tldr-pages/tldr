# copyq

> Manager de clipboard cu caracteristici avansate.
> Mai multe informaţii: <https://hluk.github.io/CopyQ/>

- Lansați CopyQ pentru a stoca istoricul clipboard-ului:

`copyq`

- Afișează conținutul curent al clipboard-ului:

`copyq clipboard`

- Introduceți text brut în istoricul clipboard-ului:

`copyq add -- {{text1}} {{text2}} {{text3}}`

- Inserați textul care conține secvențe de evacuare ('\ n','\ t') în istoricul clipboard-ului:

`copyq add {{firstline\nsecondline}}`

- Imprimați conținutul primelor 3 elemente din istoricul clipboard-ului:

`copyq read 0 1 2`

- Copiați conținutul unui fișier în clipboard:

`copyq copy < {{file.txt}}`

- Copiați o imagine JPEG în clipboard:

`copyq copy image/jpeg < {{image.jpg}}`
