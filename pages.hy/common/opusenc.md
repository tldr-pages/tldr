#աշխատանք

> Փոխարկեք WAV կամ FLAC աուդիո Opus-ի:.
> Լրացուցիչ տեղեկություններ. <https://opus-codec.org/docs/opus-tools/opusenc.html>:.

- Փոխակերպեք WAV-ը Opus-ին՝ օգտագործելով լռելյայն ընտրանքները.:

`opusenc {{path/to/input.wav}} {{path/to/output.opus}}`

- Փոխակերպեք ստերեո աուդիո ամենաբարձր որակի մակարդակով.:

`opusenc --bitrate {{512}} {{path/to/input.wav}} {{path/to/output.opus}}`

- Փոխակերպեք 5.1 շրջապատող ձայնի աուդիո ամենաբարձր որակի մակարդակով.:

`opusenc --bitrate {{1536}} {{path/to/input.flac}} {{path/to/output.opus}}`

- Փոխակերպեք խոսքի աուդիո ամենացածր որակի մակարդակով.:

`opusenc {{path/to/input.wav}} --downmix-mono --bitrate {{6}} {{path/to/out.opus}}`
