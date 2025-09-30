# virt-xml

> 명령줄 옵션을 사용하여 libvirt 도메인 XML 파일을 편집합니다.
> 참고: '도메인'은 기존 VM의 이름, UUID 또는 ID를 의미합니다 (참조: tldr virsh).
> 더 많은 정보: <https://github.com/virt-manager/virt-manager/blob/main/man/virt-xml.rst>.

- 특정 옵션에 대한 모든 하위 옵션 나열:

`virt-xml --{{옵션}}=?`

- 디스크, 네트워크 및 부트에 대한 모든 하위 옵션 나열:

`virt-xml --disk=? --network=? --boot=?`

- 특정 도메인의 값을 편집:

`virt-xml {{도메인}} --edit --{{옵션}} {{하위옵션}}={{새로운_값}}`

- 특정 도메인의 설명 변경:

`virt-xml {{도메인}} --edit --metadata description="{{새로운_설명}}"`

- 특정 도메인에 대한 부팅 장치 메뉴 활성화/비활성화:

`virt-xml {{도메인}} --edit --boot bootmenu={{on|off}}`

- 실행 중인 VM에 호스트 USB 허브 연결 (참조: tldr lsusb):

`virt-xml {{도메인}} --update --add-device --hostdev {{버스}}.{{장치}}`
