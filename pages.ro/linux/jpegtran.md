# jpegtran

> Efectuaţi transformarea fără pierderi a fişierelor JPEG.
> Mai multe informaţii: <https://manned.org/jpegtran>

- Oglindă o imagine orizontală sau verticală:

`jpegtran -flip {{horizontal|vertical}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Rotiți o imagine 90, 180 sau 270 de grade în sensul acelor de ceasornic:

`jpegtran -rotate {{90|180|270}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Transpuneți imaginea pe axa din stânga sus spre dreapta jos:

`jpegtran -transpose {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Transversați imaginea de-a lungul axei din dreapta sus spre stânga jos:

`jpegtran -transverse {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Conversia imaginii în tonuri de gri:

`jpegtran -grayscale {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Decupați imaginea într-o regiune dreptunghiulară de lățime `W` și înălțime `H` din colțul din stânga sus, salvând ieșirea într-un anumit fișier:

`jpegtran -crop {{W}}x{{H}} -outfile {{path/to/output.jpg}} {{path/to/image.jpg}}`

- Decupați imaginea într-o regiune dreptunghiulară cu lățimea „W” și înălțimea „H”, începând de la punctele „X” și „Y” din colțul din stânga sus:

`jpegtran -crop {{W}}x{{H}}+{{X}}+{{Y}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`
