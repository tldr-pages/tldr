# mosquitto_passwd

> mosquitto의 비밀번호 파일을 관리.
> 관리하는 MQTT 서버인 `mosquitto`도 참고하세요.
> 더 많은 정보: <https://mosquitto.org/man/mosquitto_passwd-1.html>.

- 비밀번호 파일에 새 사용자 추가 (비밀번호 입력을 요청함):

`mosquitto_passwd {{경로/대상/비밀번호_파일}} {{사용자명}}`

- 비밀번호 파일이 없을 경우 생성:

`mosquitto_passwd -c {{경로/대상/비밀번호_파일}} {{사용자명}}`

- 지정된 사용자명을 삭제:

`mosquitto_passwd -D {{경로/대상/비밀번호_파일}} {{사용자명}}`

- 기존의 평문 비밀번호 파일을 해시된 비밀번호 파일로 업그레이드:

`mosquitto_passwd -U {{경로/대상/비밀번호_파일}}`
