# tesseract

> motor OCR (recunoaștere optică a caracterelor).
> Mai multe informaţii: <https://github.com/tesseract-ocr/tesseract>

- Recunoașteți textul dintr-o imagine și salvați-l în `output.txt` (extensia `.txt` este adăugată automat):

`tesseract {{image.png}} {{output}}`

- Specificați o limbă personalizată (implicit este engleză) cu un cod ISO 639-2 (de exemplu, deu = Deutsch = germană):

`tesseract -l deu {{image.png}} {{output}}`

- Lista codurilor ISO 639-2 ale limbilor disponibile:

`tesseract --list-langs`

- Specificați un mod personalizat de segmentare a paginii (implicit este 3):

`tesseract -psm {{0_to_10}} {{image.png}} {{output}}`

- Lista modurilor de segmentare a paginilor și descrierile acestora:

`tesseract --help-psm`
