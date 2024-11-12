# pw-play

> PipeWire를 통해 오디오 파일 재생.
> `pw-cat --playback`의 약어.
> 같이 보기: `play`.
> 더 많은 정보: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- 기본 대상에서 WAV 사운드 파일 재생:

`pw-play {{경로/대상/파일.wav}}`

- 다른 볼륨 수준으로 WAV 사운드 파일 재생:

`pw-play --volume={{0.1}} {{경로/대상/파일.wav}}`
