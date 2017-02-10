# tesseract

> OCR (Optical Character Recognition) engine.

- Recognize text in an image and save it to a text file:

`tesseract {{image.png}} {{output.txt}}`

- Specify a custom language (default is English) with an ISO 639-2 code (e.g. deu = Deutsch = German):

`tesseract -l deu {{image.png}} {{output.txt}}`

- List the ISO 639-2 codes of available languages:

`tesseract --list-langs`

- Specify a custom page segmentation mode (default is 3):

`tesseract -psm {{0_to_10}} {{image.png}} {{output.txt}}`

- List page segmentation modes and their descriptions:

`tesseract --help-psm`
