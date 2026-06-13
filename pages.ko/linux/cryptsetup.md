# cryptsetup

> 평문 `dm-crypt` 및 LUKS (Linux Unified Key Setup) 암호화 볼륨을 관리.
> `luksFormat`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://manned.org/cryptsetup>.

- 암호를 사용하여 LUKS 볼륨 초기화 (파티션의 모든 데이터를 덮어씁니다):

`cryptsetup luksFormat {{/dev/sdXY}}`

- LUKS 볼륨을 열고 `/dev/mapper/mapping_name`에 복호화된 매핑 생성:

`cryptsetup open {{/dev/sdXY}} {{매핑_이름}}`

- 매핑에 대한 정보 표시:

`cryptsetup status {{매핑_이름}}`

- 기존 매핑 제거:

`cryptsetup close {{매핑_이름}}`

- LUKS 볼륨의 암호 변경:

`cryptsetup luksChangeKey {{/dev/sdXY}}`
