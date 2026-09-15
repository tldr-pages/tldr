# mqtt_check.py

> MQTT 로그인 자격 증명을 테스트하고 검증하는 간단한 유틸리티.
> Impacket 도구의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 대상 MQTT 브로커의 로그인 자격 증명 확인 (MQTT broker의 호스트명):

`mqtt_check.py {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상이름}}`

- 인증에 사용할 사용자 지정 Client ID 지정:

`mqtt_check.py -client-id {{클라이언트_아이디}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상이름}}`

- SSL을 사용하여 연결:

`mqtt_check.py -ssl {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상이름}}`

- 특정 포트로 연결 (기본 포트: 1883):

`mqtt_check.py -port {{포트}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상이름}}`

- 디버그 출력 활성화:

`mqtt_check.py -debug {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상이름}}`

- 도움말 표시:

`mqtt_check.py --help`
