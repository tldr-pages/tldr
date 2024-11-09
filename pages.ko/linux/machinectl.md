# machinectl

> systemd 머신 관리자를 제어합니다.
> 가상 머신, 컨테이너 및 이미지에서 작업을 실행합니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/machinectl.html>.

- `systemd-nspawn`을 사용하여 서비스를 머신으로 시작:

`sudo machinectl start {{머신_이름}}`

- 실행 중인 머신 중지:

`sudo machinectl stop {{머신_이름}}`

- 실행 중인 머신 목록 표시:

`machinectl list`

- 머신 내부에서 대화형 셸 열기:

`sudo machinectl shell {{머신_이름}}`
