# speaker-test

> ALSA를 위한 스피커 테스트 톤 생성기.
> 같이 보기: `aplay`, `arecord`, `amixer`.
> 더 많은 정보: <https://manned.org/speaker-test>.

- 핑크 노이즈로 기본 스피커 테스트:

`speaker-test`

- 사인파로 기본 스피커 테스트:

`speaker-test {{[-t|--test]}} sine {{[-f|--frequency]}} {{주파수}}`

- 미리 정의된 WAV 파일로 기본 스피커 테스트:

`speaker-test {{[-t|--test]}} wav`

- WAV 파일로 기본 스피커 테스트:

`speaker-test {{[-t|--test]}} wav {{[-w|--wavfile]}} {{경로/대상/파일}}`
