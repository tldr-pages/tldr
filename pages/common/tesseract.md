# Tesseract

> OCR (Optical Character Recognition) engine.

- Recognize text in image `image.png` and save to `output.txt` file:

`tesseract {{image.png}} {{output}}`

- Specify another language than English with a ISO 639-2 code (e.g. deu = Deutsch = German):

`tesseract -l deu {{image.png}} {{output}}`

- Specify a different page segmentation mode (e.g. Number 8: Treat image as a single word):

`tesseract -psm {{0_to_10}} {{image.png}} {{output}}`

- List page segmentation modes:

`tesseract --help-psm`

- List available languages:

`tesseract --list-langs`
