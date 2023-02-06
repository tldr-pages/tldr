# copyq

> Vágólapkezelő fejlett funkciókkal. További információ: <https://hluk.github.io/CopyQ/>.

- Indítsa el a CopyQ-t a vágólap előzményeinek tárolásához:

`copyq`

- A vágólap aktuális tartalmának megjelenítése:

`copyq clipboard`

- Nyers szöveg beillesztése a vágólap előzményeibe:

`copyq add -- {{text1}} {{text2}} {{text3}}`

- Eszcape-szekvenciákat ('\\n', '\\t') tartalmazó szöveg beillesztése a vágólap előzményeibe:

`copyq add {{firstline\nsecondline}}`

- A vágólap előzmények első 3 elemének tartalmának kinyomtatása:

`copyq read 0 1 2`

- Egy fájl tartalmának másolása a vágólapra:

`copyq copy < {{file.txt}}`

- JPEG-kép másolása a vágólapra:

`copyq copy image/jpeg < {{image.jpg}}`
