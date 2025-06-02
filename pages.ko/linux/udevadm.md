# udevadm

> Linux `udev` 관리 도구.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/udevadm.html>.

- 모든 장치 이벤트 모니터링:

`sudo udevadm monitor`

- 커널에 의해 전송된 `uevent` 출력:

`sudo udevadm monitor --kernel`

- `udev`에 의해 처리된 후의 장치 이벤트 출력:

`sudo udevadm monitor --udev`

- 장치 `/dev/sda`의 속성 나열:

`sudo udevadm info --attribute-walk {{/dev/sda}}`

- 모든 `udev` 규칙 다시 로드:

`sudo udevadm control --reload`

- 모든 `udev` 규칙 실행 트리거:

`sudo udevadm trigger`

- `/dev/sda` 로딩을 시뮬레이션하여 이벤트 실행 테스트:

`sudo udevadm test {{/dev/sda}}`
