# flac

> Encodes, decodes and tests FLAC files.
> More information: <https://xiph.org/flac>.

- Encode a WAV file to FLAC (this will create a FLAC file in the same location as the WAV file):

`flac {{path/to/file.wav}}`

- Encode a WAV file to FLAC, specifying the output file:

`flac -o {{path/to/output.flac}} {{path/to/file.wav}}`

- Decode a FLAC file to WAV, specifying the output file:

`flac -d -o {{path/to/output.wav}} {{path/to/file.flac}}`

- Test a FLAC file for the correct encoding:

`flac -t {{path/to/file.flac}}`
