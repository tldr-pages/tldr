# flac

> Encodes, decodes and tests flac files.
> More information: <https://xiph.org/flac>.

- Encode a wav file to flac (this will create a flac file in the same location as the wav file):

`flac {{path/to/file.wav}}`

- Encode a wav file to flac, specifying the output file:

`flac -o {{path/to/output.flac}} {{path/to/file.wav}}`

- Decode a flac file to wav, specifying the output file:

`flac -d -o {{path/to/output.wav}} {{path/to/file.flac}}`

- Test a flac file for the correct encoding:

`flac -t {{path/to/file.flac}}`
