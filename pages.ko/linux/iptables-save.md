# iptables-save

> `iptables` IPv4 설정 저장.
> IPv6의 경우 `ip6tables-save` 사용.
> 더 많은 정보: <https://manned.org/iptables-save>.

- `iptables` 설정 출력:

`sudo iptables-save`

- 특정 [t]테이블의 `iptables` 설정 출력:

`sudo iptables-save {{[-t|--table]}} {{테이블}}`

- `iptables` 설정을 [f]파일에 저장:

`sudo iptables-save {{[-f|--file]}} {{경로/대상/파일}}`
