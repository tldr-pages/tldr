# systool

> 버스 및 클래스별 시스템 장치 정보를 확인합니다.
> 이 명령어는 `sysfs` 패키지의 일부입니다.
> 더 많은 정보: <https://manned.org/systool>.

- 버스의 장치 속성을 모두 나열 (예: `pci`, `usb`). 모든 버스를 보려면 `ls /sys/bus` 사용:

`systool -b {{버스}} -v`

- 장치 클래스의 모든 속성을 나열 (예: `drm`, `block`). 모든 클래스를 보려면 `ls /sys/class` 사용:

`systool -c {{클래스}} -v`

- 버스의 장치 드라이버만 표시 (예: `pci`, `usb`):

`systool -b {{버스}} -D`
