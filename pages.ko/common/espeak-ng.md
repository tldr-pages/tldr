# espeak-ng

> 다국어를 지원하는 소프트웨어 음성 합성기.
> 관련 항목: `speak-ng`, `espeak`.
> 더 많은 정보: <https://github.com/espeak-ng/espeak-ng/blob/master/src/espeak-ng.1.ronn>.

- 텍스트를 음성으로 출력:

`espeak-ng "{{text}}"`

- `stdin`의 텍스트를 음성으로 출력:

`echo "{{text}}" | espeak-ng`

- 파일([f]ile) 내용을 음성으로 출력:

`espeak-ng -f {{경로/대상/파일}}`

- 특정 음성([v]oice)으로 출력:

`espeak-ng -v {{음성}} "{{텍스트}}"`

- 속도([s]peed) (기본값: 175)와 음높이([p]itch) (기본값: 50) 설정:

`espeak-ng -s {{속도}} -p {{음높이}} "{{텍스트}}"`

- 음성을 직접 재생하지 않고 [w]AV 파일로 저장:

`espeak-ng -w {{경로/대상/출력파일.wav}} "{{텍스트}}"`

- 사용 가능한 모든 음성 목록 출력:

`espeak-ng --voices`
