# Tesseract

> OCR (Optical Character Recognition) engine.

- Recognize text in image `image.png` and save to `content.txt` file:

`tesseract {{image.png}} {{content}}`

- Specify another language than English:

`tesseract -l deu {{image.png}} {{content}}`

- Specify a different page segmentation mode (e.g. Number 8: Treat image as a single word):

`tesseract -psm {{0_to_10}} {{image.png}} {{content}}`

- List page segmentation modes:

`tesseract --help-psm`

- List available languages:

`tesseract --list-langs`
