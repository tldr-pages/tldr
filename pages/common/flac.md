# flac

> Encodes, decodes and tests flac files.

- Encode a wav file to flac, writing to /path/to/file.flac:

`flac {{/path/to/file.wav}}`

- Encode a wav file to flac, specifying the output file:

`flac -o {{/path/to/output.flac}} {{/path/to/file.wav}}`

- Decode a flac file to wav, specifying the output file:

`flac -d --output-name {{/path/to/output.wav}} {{/path/to/file.flac}}`

- Test a flac file for correct encoding:

`flac -t {{/path/to/file.flac}}`
