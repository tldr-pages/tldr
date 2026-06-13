# shnsplit

> `.cue` 파일에 따라 오디오 파일을 분할합니다.
> 더 많은 정보: <http://shnutils.freeshell.org/shntool/>.

- `.wav` + `.cue` 파일을 여러 파일로 분할:

`shnsplit -f {{경로/대상/파일.cue}} {{경로/대상/파일.wav}}`

- 지원되는 형식 표시:

`shnsplit -a`

- `.flac` 파일을 여러 파일로 분할:

`shnsplit -f {{경로/대상/파일.cue}} -o flac {{경로/대상/파일.flac}}`

- `.wav` 파일을 "트랙 번호 - 앨범 - 제목" 형식으로 분할:

`shnsplit -f {{경로/대상/파일.cue}} {{경로/대상/파일.wav}} -t "%n - %a - %t"`
