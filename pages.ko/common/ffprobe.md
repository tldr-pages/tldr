# ffprobe

> 멀티미디어 스트림 분석기.
> 더 많은 정보: <https://ffmpeg.org/ffprobe.html>.

- 미디어 파일에 대해 사용 가능한 모든 스트림 정보를 표시:

`ffprobe -v error -show_streams {{입력.mp4}}`

- 미디어 지속시간 표시:

`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {{입력.mp4}}`

- 비디오의 프레임 속도 표시:

`ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 {{입력.mp4}}`

- 비디오의 너비 또는 높이를 표시:

`ffprobe -v error -select_streams v:0 -show_entries stream={{width|height}} -of default=noprint_wrappers=1:nokey=1 {{입력.mp4}}`

- 비디오의 평균 비트 전송률 표시:

`ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 {{입력.mp4}}`
