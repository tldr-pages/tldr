# rtcwake

> BIOS 시계에 상대적인 지정된 기상 시간까지 시스템을 절전 상태로 전환.
> 더 많은 정보: <https://manned.org/rtcwake>.

- 알람이 설정되었는지 여부를 확인:

`sudo rtcwake -m show -v`

- RAM에 일시 중지하고 10초 후에 기상:

`sudo rtcwake -m mem -s {{10}}`

- 디스크에 일시 중지(더 높은 전력 절약)하고 15분 후에 기상:

`sudo rtcwake -m disk --date +{{15}}min`

- 시스템을 동결(램에 일시 중지보다 더 효율적이며 Linux 커널 버전 3.9 이상 필요)하고 지정된 날짜와 시간에 기상:

`sudo rtcwake -m freeze --date {{YYYYMMDDhhmm}}`

- 이전에 설정한 알람 비활성화:

`sudo rtcwake -m disable`

- 주어진 시간에 컴퓨터를 깨우는 드라이 런 수행. (중단하려면 `<Ctrl c>`를 누르세요):

`sudo rtcwake -m on --date {{hh:ss}}`
