# sfdisk

> 디스크 파티션 테이블을 표시하거나 조작합니다.
> 더 많은 정보: <https://manned.org/sfdisk>.

- 파티션 레이아웃을 파일로 백업:

`sudo sfdisk {{[-d|--dump]}} {{경로/대상/장치}} > {{경로/대상/파일.dump}}`

- 파티션 레이아웃 복원:

`sudo sfdisk {{경로/대상/장치}} < {{경로/대상/파일.dump}}`

- 파티션 유형 설정:

`sfdisk --part-type {{경로/대상/장치}}} {{파티션_번호}} {{swap}}`

- 파티션 삭제:

`sfdisk --delete {{경로/대상/장치}} {{파티션_번호}}`

- 도움말 표시:

`sfdisk {{[-h|--help]}}`
