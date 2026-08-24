# gphoto2

> 명령줄에서 디지털 카메라를 제어.
> 더 많은 정보: <http://www.gphoto.org/doc/manual/ref-gphoto2-cli.html>.

- 연결된 카메라 목록 표시:

`gphoto2 --auto-detect`

- 카메라의 파일 목록 표시:

`gphoto2 {{[-L|--list-files]}}`

- 모든 이미지 다운로드:

`gphoto2 {{[-P|--get-all-files]}}`

- 새로운 이미지만 다운로드 (기존 파일은 건너뜀):

`gphoto2 {{[-P|--get-all-files]}} --new`

- 1부터 5까지 지정한 범위의 파일만 다운로드:

`gphoto2 {{[-p|--get-file]}} 1-5`

- 카메라의 모든 파일 삭제:

`gphoto2 {{[-D|--delete-all-files]}}`

- 사진을 촬영하고 즉시 다운로드:

`gphoto2 --capture-image-and-download`

- 카메라 정보 표시:

`gphoto2 --summary`
