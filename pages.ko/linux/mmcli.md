# mmcli

> ModemManager를 제어하고 모니터링.
> 더 많은 정보: <https://www.freedesktop.org/software/ModemManager/man/latest/mmcli.1.html>.

- 사용 가능한 모뎀 나열:

`mmcli --list-modems`

- 모뎀에 대한 정보 출력:

`mmcli --modem={{모뎀}}`

- 모뎀 활성화:

`mmcli --modem={{모뎀}} --enable`

- 모뎀에서 사용 가능한 SMS 메시지 나열:

`sudo mmcli --modem={{모뎀}} --messaging-list-sms`

- 모뎀에서 메시지를 삭제, 경로 지정:

`sudo mmcli --modem={{모뎀}} --messaging-delete-sms={{경로/대상/메시지_파일}}`
