# transcode

> 비디오 및 오디오 코덱을 변환하고 미디어 형식을 변환하는 도구.
> 더 많은 정보: <https://manned.org/transcode>.

- 카메라 흔들림 제거를 위한 안정화 파일 생성:

`transcode -J stabilize -i {{입력_파일}}`

- 안정화 파일 생성 후 카메라 흔들림 제거, XviD를 사용하여 비디오 변환:

`transcode -J transform -i {{입력_파일}} -y xvid -o {{출력_파일}}`

- 비디오 크기를 640x480 픽셀로 조정하고 XviD를 사용하여 MPEG4 코덱으로 변환:

`transcode -Z 640x480 -i {{입력_파일}} -y xvid -o {{출력_파일}}`
