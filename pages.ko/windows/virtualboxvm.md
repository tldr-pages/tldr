# virtualboxvm

> VirtualBox 가상 머신을 관리합니다.
> 더 많은 정보: <https://www.virtualbox.org>.

- 가상 머신 시작:

`virtualboxvm --startvm {{이름|uuid}}`

- 전체 화면 모드로 가상 머신 시작:

`virtualboxvm --startvm {{이름|uuid}} --fullscreen`

- 지정된 DVD 이미지 파일 마운트:

`virtualboxvm --startvm {{이름|uuid}} --dvd {{경로\대상\이미지_파일}}`

- 디버그 정보가 포함된 명령줄 창 표시:

`virtualboxvm --startvm {{이름|uuid}} --debug-command-line`

- 일시 중지된 상태로 가상 머신 시작:

`virtualboxvm --startvm {{이름|uuid}} --start-paused`
