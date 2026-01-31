# dhcpcd

> DHCP 클라이언트.
> 더 많은 정보: <https://roy.marples.name/projects/dhcpcd>.

- 모든 주소 임대 해제:

`sudo dhcpcd {{[-k|--release]}}`

- DHCP 서버에 새 임대 요청:

`sudo dhcpcd {{[-n|--rebind]}}`

- 지정한 인터페이스의 마지막으로 획득한 임대를 출력하고 종료:

`sudo dhcpcd {{[-U|--dumplease]}} {{interface_name}}`
