# tlp-stat

> TLP 상태 보고서 생성.
> 같이 보기: `tlp`.
> 더 많은 정보: <https://linrunner.de/tlp/usage/tlp-stat>.

- 구성 및 모든 활성 설정으로 상태 보고서 생성:

`sudo tlp-stat`

- 다양한 장치에 대한 정보 표시:

`sudo tlp-stat --{{battery|disk|processor|graphics|pcie|rfkill|usb}}`

- 장치에 대해 자세한 정보 표시(자세한 정보 지원 장치만):

`sudo tlp-stat --verbose --{{battery|processor|pcie|usb}}`

- 구성 표시:

`sudo tlp-stat {{[-c|--config]}}`

- 전원 공급 `udev` 이벤트 모니터링:

`sudo tlp-stat {{[-P|--pev]}}`

- 전원 공급 진단 표시:

`sudo tlp-stat --psup`

- 온도 및 팬 속도 표시:

`sudo tlp-stat {{[-t|--temp]}}`

- 일반 시스템 정보 표시:

`sudo tlp-stat {{[-s|--system]}}`
