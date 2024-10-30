# gpg-card

> OpenPGP 및 PIV 스마트 카드를 관리.
> `gpg --card-edit`과 유사.
> 더 많은 정보: <https://manned.org/gpg-card>.

- 대화형 모드에서 시작:

`gpg-card`

- 비대화식으로 하나 이상의 명령을 호출:

`gpg-card {{명령어1}} -- {{명령어2}} -- {{명령어3}}`

- 스마트 카드에 대한 정보 표시:

`gpg-card list`

- OpenPGP 카드에 저장된 URL을 사용하여 공개 키를 검색:

`gpg-card fetch`

- `fetch` 명령어에 사용되는 URL을 설정:

`gpg-card url`

- PIN 변경 또는 차단 해제 (비대화형 모드에서 카드에 대한 기본 작업을 사용):

`gpg-card passwd`

- OpenPGP 카드의 forcesig 플래그를 토글 (즉, 서명을 위해 사용자 PIN을 입력해야 함):

`gpg-card forcesig`

- 스마트 카드 공장 초기화 (예. 모든 데이터 삭제 및 PIN 재설정):

`gpg-card factory-reset`
