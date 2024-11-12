# pw-record

> PipeWire를 통해 오디오 파일을 녹음.
> `pw-cat --record`의 축약형.
> 더 많은 정보: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- 기본 대상 장치를 사용하여 샘플 녹음:

`pw-record {{경로/대상/파일.wav}}`

- 다른 볼륨 레벨로 샘플 녹음:

`pw-record --volume={{0.1}} {{경로/대상/파일.wav}}`

- 다른 샘플 속도를 사용하여 샘플 녹음:

`pw-record --rate={{6000}} {{경로/대상/파일.wav}}`
