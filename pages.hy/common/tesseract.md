# թեսերակտ

> OCR (Optical Character Recognition) շարժիչ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc>:.

- Ճանաչեք պատկերի տեքստը և պահեք այն տրված ճանապարհին (`.txt` ընդլայնումն ավտոմատ կերպով ավելացվում է).:

`tesseract {{path/to/image.png}} {{path/to/output_file}}`

- Նշեք հատուկ [l]լեզու (կանխադրվածը անգլերենն է) ISO 639-2 կոդով (օրինակ՝ deu = Deutsch = գերմաներեն):

`tesseract -l deu {{path/to/image.png}} {{path/to/output_file}}`

- Թվարկե՛ք տեղադրված լեզուների ISO 639-2 ծածկագրերը.:

`tesseract --list-langs`

- Նշեք հատուկ [p]age [s]egmentation [m] ռեժիմ (կանխադրվածը 3 է):

`tesseract --psm {{0..13}} {{path/to/image.png}} {{path/to/output_file}}`

- Նշեք էջի հատվածավորման ռեժիմները և դրանց նկարագրությունները.:

`tesseract --help-psm`
