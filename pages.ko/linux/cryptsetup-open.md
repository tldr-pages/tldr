# cryptsetup open

> 암호화된 볼륨의 암호 해독된 매핑 생성.
> 참고: TRIM이 활성화된 경우, 해방된 블록 정보의 형태로 최소한의 데이터 누출이 발생할 수 있으며, 사용 중인 파일 시스템을 파악하는 데 충분할 수 있습니다.
> 그러나 데이터 자체는 여전히 안전하며, TRIM이 없는 SSD는 더 빨리 마모되므로 TRIM을 활성화하는 것이 좋습니다.
> 더 많은 정보: <https://manned.org/cryptsetup-open>.

- LUKS 볼륨을 열고 `/dev/mapper/{{매핑_이름}}`에 암호 해독된 매핑 생성:

`cryptsetup open {{/dev/sdXY}} {{매핑_이름}}`

- 암호 대신 키 파일 사용:

`cryptsetup open --key-file {{경로/대상/파일}} {{/dev/sdXY}} {{매핑_이름}}`

- 장치에서 TRIM 사용 허용:

`cryptsetup open --allow-discards {{/dev/sdXY}} {{매핑_이름}}`

- LUKS 헤더에 `--allow-discards` 옵션 기록 (장치를 열 때마다 항상 이 옵션 사용):

`cryptsetup open --allow-discards --persistent {{/dev/sdXY}} {{매핑_이름}}`

- LUKS 볼륨을 열고 암호 해독된 매핑을 읽기 전용으로 설정:

`cryptsetup open --readonly {{/dev/sdXY}} {{매핑_이름}}`
