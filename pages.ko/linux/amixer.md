# amixer

> ALSA 사운드 카드 드라이버의 믹서.
> 더 많은 정보: <https://manned.org/amixer>.

- 마스터 볼륨을 10% 높이기:

`amixer -D pulse sset Master {{10%+}}`

- 마스터 볼륨을 10% 낮추기:

`amixer -D pulse sset Master {{10%-}}`
