# tesseract

> OCR (Optical Character Recognition) engine.
> More information: <https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc>.

- Recognize text in an image and save it to the given path (a `.txt` extension is added automatically):

`tesseract {{path/to/image.png}} {{path/to/output_file}}`

- Specify a custom [l]anguage (default is English) with an ISO 639-2 code (e.g. deu = Deutsch = German):

`tesseract -l deu {{path/to/image.png}} {{path/to/output}}`

- List the ISO 639-2 codes of installed languages:

`tesseract --list-langs`

- Specify a custom [p]age [s]egmentation [m]ode (default is 3):

`tesseract --psm {{0..13}} {{path/to/image.png}} {{path/to/output}}`

- List page segmentation modes and their descriptions:

`tesseract --help-psm`
