# kdeconnect-cli

> 파일이나 텍스트를 장치에 공유하거나, 벨소리를 울리거나, 잠금을 해제하는 등 여러 작업을 수행하기 위해 KDE Connect를 사용하세요.
> 더 많은 정보: <https://kdeconnect.kde.org>.

- 모든 장치 나열:

`kdeconnect-cli --list-devices`

- 사용 가능한 장치(페어링되고 접근 가능한) 나열:

`kdeconnect-cli --list-available`

- 특정 장치와 페어링 요청, 장치 ID 지정:

`kdeconnect-cli --pair --device {{장치_ID}}`

- 장치의 벨소리를 울리기, 장치 이름 지정:

`kdeconnect-cli --ring --name "{{장치_이름}}"`

- URL 또는 파일을 페어링된 장치와 공유, 장치 ID 지정:

`kdeconnect-cli --share {{url|경로/대상/파일}} --device {{장치_ID}}`

- 선택적 첨부 파일과 함께 특정 번호로 SMS 보내기:

`kdeconnect-cli --name "{{장치_이름}}" --send-sms "{{메시지}}" --destination {{전화번호}} --attachment {{경로/대상/파일}}`

- 특정 장치 잠금 해제:

`kdeconnect-cli --name "{{장치_이름}}" --unlock`

- 특정 장치에서 키 입력 시뮬레이션:

`kdeconnect-cli --name "{{장치_이름}}" --send-keys {{키}}`
