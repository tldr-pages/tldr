# euse

> Gentoo USE 플래그를 활성화, 비활성화하거나 정보를 조회.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Euse>.

- 활성화된 전역 USE 플래그 목록 표시:

`euse {{[-a|--active]}} {{[-g|--global]}}`

- 활성화된 로컬 USE 플래그 목록 표시:

`euse {{[-a|--active]}} {{[-l|--local]}}`

- 전역 USE 플래그 활성화:

`sudo euse {{[-E|--enable]}} {{use_플래그}}`

- 전역 USE 플래그 비활성화 (USE 플래그 이름 앞에 '-'를 추가):

`sudo euse {{[-D|--disable]}} {{use_플래그}}`

- 전역 USE 플래그 제거:

`sudo euse {{[-P|--prune]}} {{use_플래그}}`
