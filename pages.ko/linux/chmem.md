# chmem

> Linux 시스템에서 메모리 블록 상태(online/offline) 변경.
> 주로 가상화 환경에서 메모리 핫플러그(hotplug) 관리에 사용.
> 더 많은 정보: <https://manned.org/chmem>.

- 메모리 블록을 offline 상태로 설정:

`sudo chmem {{[-b|--block]}} {{[-d|--disable]}} {{블록_번호}}`

- 메모리 블록을 online 상태로 설정:

`sudo chmem {{[-b|--block]}} {{[-e|--enable]}} {{블록_번호}}`

- 16진수 주소 범위를 사용하여 메모리 영역을 offline 상태로 설정:

`sudo chmem {{[-d|--disable]}} 0x{{시작_주소}}-0x{{end_address}}`

- 16진수 주소 범위를 사용하여 메모리 영역을 online 상태로 설정:

`sudo chmem {{[-e|--enable]}} 0x{{시작_주소}}-0x{{end_address}}`

- 메모리를 online 상태로 설정하고 특정 존(예: Movable)에 할당:

`sudo chmem {{[-e|--enable]}} 0x{{시작_주소}} {{[-z|--zone]}} {{Movable}}`

- 도움말 표시:

`chmem {{[-h|--help]}}`
