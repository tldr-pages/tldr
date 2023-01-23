# tesseract

> OCR (optikai karakterfelismerő) motor. További információ: <https://github.com/tesseract-ocr/tesseract>.

- Felismeri a szöveget egy képen, és elmenti a `output.txt` címre (a `.txt` kiterjesztés automatikusan hozzáadódik):

`tesseract {{image.png}} {{output}}`

- Egyéni nyelv megadása (alapértelmezett az angol) ISO 639-2 kóddal (pl. deu = Deutsch = német):

`tesseract -l deu {{image.png}} {{output}}`

- A rendelkezésre álló nyelvek ISO 639-2 kódjainak felsorolása:

`tesseract --list-langs`

- Egyéni oldalszegmentálási mód megadása (alapértelmezett: 3):

`tesseract -psm {{0_to_10}} {{image.png}} {{output}}`

- Az oldalszegmentálási módok és leírásuk felsorolása:

`tesseract --help-psm`
