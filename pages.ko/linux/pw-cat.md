# pw-cat

> PipeWire를 통해 오디오 파일을 재생하고 녹음.
> 더 많은 정보: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- 기본 대상으로 WAV 파일 재생:

`pw-cat {{[-p|--playback]}} {{경로/대상/파일.wav}}`

- 지정된 리샘플러 품질(기본값 4)로 WAV 파일 재생:

`pw-cat {{[-q|--quality]}} {{0..15}} {{[-p|--playback]}} {{경로/대상/파일.wav}}`

- 125% 볼륨 수준으로 샘플 녹음:

`pw-cat {{[-r|--record]}} --volume {{1.25}} {{경로/대상/파일.wav}}`

- 다른 샘플 레이트를 사용하여 샘플 녹음:

`pw-cat {{[-r|--record]}} --rate {{6000}} {{경로/대상/파일.wav}}`

- 도움말 표시:

`pw-cat {{[-h|--help]}}`
