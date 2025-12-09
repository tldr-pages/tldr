# bluetoothd

> 블루투스 장치를 관리하는 데몬.
> 더 많은 정보: <https://manned.org/bluetoothd>.

- 데몬 시작:

`bluetoothd`

- 로그를 `stdout`으로 출력하며 데몬 시작:

`bluetoothd --nodetach`

- 특정 설정 파일을 사용하여 데몬 시작 (기본값은 `/etc/bluetooth/main.conf`):

`bluetoothd --configfile {{경로/대상/파일}}`

- 자세한 출력을 `stderr`로 출력하며 데몬 시작:

`bluetoothd --debug`

- bluetoothd 또는 플러그인 소스의 특정 파일에서 오는 자세한 출력을 사용하여 데몬 시작:

`bluetoothd --debug={{경로/대상/파일1:경로/대상/파일2:...}}`
