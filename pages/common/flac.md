# flac

> Encodes, decodes and tests flac files.


- Encode a wav file to flac, writing to /path/to/file.flac:

`flac {{/path/to/file.wav}}`

- Decode a flac file to wav, specifying the output file:

`flac -d --output-name {{/path/to/output.wav}} {{/path/to/input.flac}}`

- Test a flac file:

`flac -t {{/path/to/file.flac}}`
