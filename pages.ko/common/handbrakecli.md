# handbrakecli

> HandBrake 비디오 변환 및 DVD 리핑 도구에 대한 명령줄 인터페이스.
> 더 많은 정보: <https://handbrake.fr/docs/en/latest/cli/command-line-reference.html>.

- 비디오 파일을 MKV(AAC 160kbit 오디오 및 x264 CRF20 비디오)로 변환:

`handbrakecli {{[-i|--input]}} {{입력.avi}} {{[-o|--output]}} {{출력.mkv}} {{[-e|--encoder]}} x264 {{[-q|--quality]}} 20 {{[-B|--ab]}} 160`

- 비디오 파일 크기를 320x240으로 조정:

`handbrakecli {{[-i|--input]}} {{입력.mp4}} {{[-o|--output]}} {{출력.mp4}} {{[-w|--width]}} 320 {{[-l|--height]}} 240`

- 사용 가능한 사전 설정 목록:

`handbrakecli {{[-z|--preset-list]}}`

- Android 사전 설정을 사용하여 AVI 비디오를 MP4로 변환:

`handbrakecli {{[-Z|--preset]}} "Android" {{[-i|--input]}} {{입력.ext}} {{[-o|--output]}} {{출력.mp4}}`

- DVD 내용을 출력하고 그 과정에서 CSS 키를 가져옴:

`handbrakecli {{[-i|--input]}} {{/dev/sr0}} {{[-t|--title]}} 0`

- 지정된 장치에서 DVD의 첫 번째 트랙을 추출. 오디오트랙과 자막 언어는 목록으로 지정됨:

`handbrakecli {{[-i|--input]}} {{/dev/sr0}} {{[-t|--title]}} 1 {{[-o|--output]}} {{out.mkv}} {{[-f|--format]}} av_mkv {{[-e|--encoder]}} x264 {{[-s|--subtitle]}} {{1,4,5}} {{[-a|--audio]}} {{1,2}} {{[-E|--aencoder]}} copy {{[-q|--quality]}} {{23}}`
