# gpu-screen-recorder

> GPU를 사용하여 화면을 녹화하고 비디오를 인코딩.
> 더 많은 정보: <https://git.dec05eba.com/gpu-screen-recorder/about/>.

- 데스크톱 포털을 통해 녹화 대상을 선택하여 녹화:

`gpu-screen-recorder -w portal -o {{경로/대상/비디오.mp4}}`

- 지정한 화면 또는 디스플레이 녹화:

`gpu-screen-recorder -w {{screen|DP-1|HDMI-A1|...}} -o {{경로/대상/비디오.mp4}}`

- 사용 가능한 비디오 캡처 대상 목록 표시:

`gpu-screen-recorder --list-capture-options`

- 사용 가능한 오디오 캡처 대상 목록 표시:

`gpu-screen-recorder {{--list-audio-devices|--list-application-audio}}`

- 리플레이 버퍼를 사용하여 녹화:

`gpu-screen-recorder -w {{스크린}} -r {{30}} -c {{mp4}} -ro {{경로/대상/디렉터리}} -o {{whatever}}`

- 리플레이 버퍼를 사용하여 비디오 녹화:

`pkill -SIGUSR1 -f gpu-screen-recorder`

- `gpu-screen-recorder`를 백그라운드에서 실행:

`systemctl start --user gpu-screen-recorder`
