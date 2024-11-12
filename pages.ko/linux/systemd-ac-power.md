# systemd-ac-power

> 컴퓨터가 외부 전원에 연결되어 있는지 보고.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-ac-power.html>.

- 조용히 확인하고 AC 전원에 연결되어 있을 때 0 상태 코드를 반환하고, 그렇지 않을 경우 비영 상태 코드를 반환:

`systemd-ac-power`

- 추가적으로 `stdout`에 `yes` 또는 `no`를 출력:

`systemd-ac-power --verbose`
