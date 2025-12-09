# vgmstream_cli

> 다양한 비디오 게임 오디오 포맷을 재생하고 `wav`로 변환.
> 더 많은 정보: <https://github.com/vgmstream/vgmstream/blob/master/doc/USAGE.md>.

- `adc` 파일을 `wav`로 디코딩 (기본 출력 이름은 `input.wav`):

`vgmstream_cli {{경로/대상/입력.adc}} -o {{경로/대상/출력.wav}}`

- 오디오를 디코딩하지 않고 메타데이터 출력:

`vgmstream_cli {{경로/대상/입력.adc}} -m`

- 루프 없이 오디오 파일 디코딩:

`vgmstream_cli {{경로/대상/입력.adc}} -o {{경로/대상/출력.wav}} -i`

- 세 번의 루프로 디코딩한 후 3초 지연 및 5초 페이드아웃 추가:

`vgmstream_cli {{경로/대상/입력.adc}} -o {{경로/대상/출력.wav}} -l {{3.0}} -f {{5.0}} -d {{3.0}}`

- 여러 파일을 `bgm_(원래 이름).wav`로 변환 (기본 `-o` 패턴은 `?f.wav`):

`vgmstream_cli -o {{경로/대상/bgm_?f.wav}} {{경로/대상/파일1.adc}} {{경로/대상/파일2.adc}}`

- 파일을 무한 반복으로 재생 (`channels`와 `rate`는 메타데이터와 일치해야 함):

`vgmstream_cli {{경로/대상/입력.adc}} -pec | aplay --format cd --channels {{1}} --rate {{44100}}`
