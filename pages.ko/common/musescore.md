# musescore

> MuseScore 3 악보 편집기.
> 같이 보기: `lilypond`.
> 더 많은 정보: <https://handbook.musescore.org/appendix/command-line-usage>.

- 특정 오디오 드라이버 사용:

`musescore --audio-driver {{jack|alsa|portaudio|pulse}}`

- MP3 출력 비트레이트를 kbit/s 단위로 설정:

`musescore --bitrate {{비트레이트}}`

- MuseScore를 디버그 모드로 시작:

`musescore --debug`

- 레이어와 같은 실험적 기능 활성화:

`musescore --experimental`

- 주어진 파일을 지정된 출력 파일로 내보내기. 파일 유형은 주어진 확장자에 따라 결정됨:

`musescore --export-to {{출력_파일}} {{입력_파일}}`

- 주어진 악보 간의 차이를 출력:

`musescore --diff {{경로/대상/파일1}} {{경로/대상/파일2}}`

- MIDI 가져오기 작업 파일 지정:

`musescore --midi-operations {{경로/대상/파일}}`
