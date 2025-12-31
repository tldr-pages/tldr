# arecord

> ALSA 사운드카드 드라이버용 사운드 레코더.
> 더 많은 정보: <https://manned.org/arecord>.

- "CD" 품질로 녹음 (완료 시 `<Ctrl c>`로 종료):

`arecord -vv --format=cd {{경로/대상/파일.wav}}`

- "CD" 품질로 10초 동안 고정된 길이로 녹음:

`arecord -vv --format=cd --duration={{10}} {{경로/대상/파일.wav}}`

- 녹음하여 MP3로 저장 (완료 시 `<Ctrl c>`로 종료):

`arecord -vv --format=cd --file-type raw | lame -r - {{경로/대상/파일.mp3}}`

- 모든 사운드 카드와 디지털 오디오 장치 나열:

`arecord --list-devices`

- 인터랙티브 인터페이스 허용 (예: `<Space>` `<Enter>` 재생 또는 일시 정지):

`arecord --interactive`

- 마이크 테스트를 위해 5초 샘플을 녹음하고 재생:

`arecord -d 5 test-mic.wav && aplay test-mic.wav && rm test-mic.wav`
