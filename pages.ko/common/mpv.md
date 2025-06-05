# mpv

> MPlayer 기반의 오디오/비디오 플레이어.
> 같이 보기: `mplayer`, `vlc`.
> 더 많은 정보: <https://mpv.io/manual/stable/>.

- URL 또는 파일에서 비디오나 오디오 재생:

`mpv {{url|경로/대상/파일}}`

- 5초 뒤로/앞으로 이동:

`{{<ArrowLeft>|<ArrowRight>}}`

- 1분 뒤로/앞으로 이동:

`{{<ArrowDown>|<ArrowUp>}}`

- 재생 속도를 10% 감소/증가:

`{{<[>|<]>}}`

- 현재 프레임의 스크린샷 찍기 (기본적으로 `./mpv-shotNNNN.jpg`에 저장됨):

`<s>`

- 지정된 속도로 파일 재생 (기본값은 1):

`mpv --speed {{0.01..100}} {{경로/대상/파일}}`

- `mpv.conf` 파일에 정의된 프로필을 사용하여 파일 재생:

`mpv --profile {{프로필_이름}} {{경로/대상/파일}}`

- 웹캠 또는 다른 비디오 입력 장치의 출력 표시:

`mpv {{/dev/video0}}`
