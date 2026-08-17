# wmpconfig

> Windows Media Player (legacy)의 네트워크 공유를 관리.
> 참고: 이 명령은 관리자 권한이 필요함.
> 관련 항목: `wmpnscfg`.
> 더 많은 정보: <https://learn.microsoft.com/previous-versions/windows/desktop/wmp/command-line-parameters>.

- 네트워크 공유 기능 활성화 또는 비활성화:

`wmpconfig {{HMEOn|HMEOff}}`

- 지정한 MAC 주소의 네트워크 장치가 이 컴퓨터와 공유하지 못하도록 설정:

`wmpconfig DisableHMEDevice {{mac_주소}}`

- 지정한 네트워크 장치를 이 컴퓨터와의 공유 대상에서 제거:

`wmpconfig RemoveHMEDevice {{mac_주소}}`

- 지정한 네트워크 장치와의 공유 복원:

`wmpconfig RestoreHMEDevice {{mac_주소}}`

- DVD 콘텐츠 재생을 위한 자녀 보호 수준 설정:

`wmpconfig SetDVDParentalLevel {{3}}`
