# bcachefs device

> 실행 중인 `bcachefs` 파일 시스템 내에서 장치를 관리합니다.
> 더 많은 정보: <https://bcachefs-docs.readthedocs.io/en/latest/mgmt-devicemanagement.html>.

- 기존 파일 시스템에 새 장치를 포맷하고 추가:

`sudo bcachefs device add --label={{그룹}}.{{이름}} {{경로/대상/마운트_포인트}} {{경로/대상/장치}}`

- 제거를 준비하기 위해 장치의 데이터를 마이그레이션:

`bcachefs device evacuate {{경로/대상/장치}}`

- 파일 시스템에서 장치를 영구적으로 제거:

`bcachefs device remove {{경로/대상/장치}}`
