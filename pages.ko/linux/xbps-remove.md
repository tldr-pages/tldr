# xbps-remove

> 패키지를 제거하는 XBPS 유틸리티.
> 같이 보기: `xbps`.
> 더 많은 정보: <https://manned.org/xbps-remove.1>.

- 패키지 제거:

`xbps-remove {{패키지}}`

- 패키지와 그 의존성 제거:

`xbps-remove --recursive {{패키지}}`

- 고아 패키지 제거 (의존성으로 설치되었지만 더 이상 어떤 패키지도 필요로 하지 않는 패키지):

`xbps-remove --remove-orphans`

- 캐시에서 오래된 패키지 제거:

`xbps-remove --clean-cache`
