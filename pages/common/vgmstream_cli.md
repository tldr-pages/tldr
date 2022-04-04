# vgmstream CLI decoder

> Software for playing a wide variety of audio formats used in video games.
> Converts playable files to wav.
> More information: <https://vgmstream.org/doc/USAGE>.

- Decode a adc file to wav. (Default output name is `input.wav`):

`vgmstream_cli {{input.adc}} -o {{output.wav}}`

- Print metadata without decoding the audio:

`vgmstream_cli {{input.adc}} -m`

- Decode audio without loops:

`vgmstream_cli {{input.adc}} -o {{output.wav}} -i`

- Decode with three loops, then add a 3s delay followed by a 5s fadeout:

`vgmstream_cli {{input.adc}} -o {{output.wav}} -l 3.0 -f 5.0 -d 3.0`

- Convert multiple files to `bgm_(name).wav` (Default is `?f.wav`):

`vgmstream_cli -o {{bgm_?f.wav}} {{file1.adc}} {{file2.adc}}`

- Play the file looping endlessly (`channels` and `rate` must match metadata):

`vgmstream_cli {{input.adc}} -pec | aplay --format cd --channels {{1}} --rate {{44100}}`
