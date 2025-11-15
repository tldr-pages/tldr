# cryptsetup luksFormat

> LUKS 파티션과 초기 키 슬롯(0)을 암호 또는 키파일로 초기화합니다.
> 참고: 이 작업은 파티션의 모든 데이터를 덮어씁니다.
> 더 많은 정보: <https://manned.org/cryptsetup-luksFormat>.

- 암호로 LUKS 볼륨 초기화:

`cryptsetup luksFormat {{/dev/sdXY}}`

- 키파일로 LUKS 볼륨 초기화:

`cryptsetup luksFormat {{/dev/sdXY}} {{경로/대상/키파일}}`

- 암호로 LUKS 볼륨 초기화하고 라벨 설정:

`cryptsetup luksFormat --label {{라벨}} {{/dev/sdXY}}`
