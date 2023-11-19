# vgmstream_cli

> Play a wide variety of audio formats used in video games and convert them into `wav`.
> More information: <https://github.com/vgmstream/vgmstream/blob/master/doc/USAGE.md>.

- Decode an `adc` file to `wav`. (Default output name is `input.wav`):

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}}`

- Print metadata without decoding the audio:

`vgmstream_cli {{path/to/input.adc}} -m`

- Decode an audio file without loops:

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}} -i`

- Decode with three loops, then add a 3s delay followed by a 5s fadeout:

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}} -l {{3.0}} -f {{5.0}} -d {{3.0}}`

- Convert multiple files to `bgm_(original name).wav` (Default `-o` pattern is `?f.wav`):

`vgmstream_cli -o {{path/to/bgm_?f.wav}} {{path/to/file1.adc}} {{path/to/file2.adc}}`

- Play the file looping endlessly (`channels` and `rate` must match metadata):

`vgmstream_cli {{path/to/input.adc}} -pec | aplay --format cd --channels {{1}} --rate {{44100}}`
