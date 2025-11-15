# zramctl

> zram 장치를 설정하고 제어.
> `mkfs` 또는 `mkswap`를 사용하여 zram 장치를 파티션으로 포맷하세요.
> 더 많은 정보: <https://manned.org/zramctl>.

- zram이 활성화되어 있는지 확인:

`lsmod | grep -i zram`

- 동적 장치 수로 zram 활성화 (`zramctl`을 사용하여 장치를 추가로 구성):

`sudo modprobe zram`

- 정확히 2개의 장치로 zram 활성화:

`sudo modprobe zram num_devices={{2}}`

- 다음 사용 가능한 zram 장치를 찾아 LZ4 압축을 사용하여 2GB 가상 드라이브로 초기화:

`sudo zramctl --find --size {{2GB}} --algorithm {{lz4}}`

- 현재 초기화된 장치 나열:

`sudo zramctl`
