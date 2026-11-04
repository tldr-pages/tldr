# iscsiadm

> iSCSI 세션, 노드 및 대상 검색을 관리.
> 더 많은 정보: <https://manned.org/iscsiadm>.

- 활성 iSCSI 세션 목록 표시:

`sudo iscsiadm {{[-m|--mode]}} session`

- 알려진 모든 iSCSI 노드 목록 표시:

`sudo iscsiadm {{[-m|--mode]}} node`

- 포털에서 사용 가능한 iSCSI 대상 검색 (인증 없음):

`sudo iscsiadm {{[-m|--mode]}} discovery {{[-t|--type]}} sendtargets {{[-p|--portal]}} {{ip_주소}}`

- 인증 없이 지정한 iSCSI 대상에 로그인:

`sudo iscsiadm {{[-m|--mode]}} node {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_주소}}:3260 {{[-l|--login]}}`

- 지정한 iSCSI 대상에서 로그아웃:

`sudo iscsiadm {{[-m|--mode]}} node {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_주소}}:3260 {{[-u|--logout]}}`

- 대상 검색이 차단된 경우(CHAP 인증용) iSCSI 노드 생성:

`sudo iscsiadm {{[-m|--mode]}} node {{[-o|--op]}} new {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_주소}}:3260`

- iSCSI 대상에 대해 CHAP 인증 설정:

`sudo iscsiadm {{[-m|--mode]}} node {{[-T|--targetname]}} {{iqn}} {{[-p|--portal]}} {{ip_주소}}:3260 {{[-o|--op]}} update {{[-n|--name]}} node.session.auth.authmethod {{[-v|--value]}} CHAP`
