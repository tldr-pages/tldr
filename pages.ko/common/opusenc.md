# opusenc

> WAV 또는 FLAC 오디오를 Opus로 변환.
> 더 많은 정보: <https://opus-codec.org/docs/opus-tools/opusenc.html>.

- 기본 옵션을 사용하여 WAV를 Opus로 변환:

`opusenc {{경로/대상/입력.wav}} {{경로/대상/출력.opus}}`

- 스테레오 오디오를 최고 품질 수준으로 변환:

`opusenc --bitrate {{512}} {{경로/대상/입력.wav}} {{경로/대상/출력.opus}}`

- 5.1 서라운드 사운드 오디오를 최고 품질 수준으로 변환:

`opusenc --bitrate {{1536}} {{경로/대상/입력.flac}} {{경로/대상/출력.opus}}`

- 음성 오디오를 최저 품질 수준으로 변환:

`opusenc {{경로/대상/입력.wav}} --downmix-mono --bitrate {{6}} {{경로/대상/출력.opus}}`
