# iwinfo

> OpenWrt에서 무선 인터페이스 정보를 조회.
> 더 많은 정보: <https://openwrt.org/docs/guide-developer/ubus/iwinfo>.

- 사용 가능한 모든 무선 인터페이스 목록 표시:

`iwinfo`

- 지정한 무선 인터페이스의 상세 정보 표시:

`iwinfo {{인터페이스}} info`

- 지정한 무선 인터페이스에서 주변 무선 네트워크 검색:

`iwinfo {{인터페이스}} scan`

- 연결된 장치 목록 표시:

`iwinfo {{인터페이스}} assoclist`

- 인터페이스에서 지원하는 채널 목록 표시:

`iwinfo {{인터페이스}} freqlist`

- 인터페이스에서 사용할 수 있는 송신 출력 목록 표시:

`iwinfo {{인터페이스}} txpowerlist`

- 도움말 표시:

`iwinfo h`
