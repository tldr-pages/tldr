# extundelete

> 저널을 분석하여 ext3 또는 ext4 파티션에서 삭제된 파일을 복구합니다.
> Unix 시간 정보는 `date`, 파티션을 마운트 해제하려면 `umount`도 참조하세요.
> 더 많은 정보: <https://extundelete.sourceforge.net/options.html>.

- 디바이스 X의 파티션 N 안의 모든 삭제된 파일 복구:

`sudo extundelete {{/dev/sdXN}} --restore-all`

- 루트에 상대적인 경로에서 파일 복구(경로를 `/`로 시작하지 마세요):

`extundelete {{/dev/sdXN}} --restore-file {{경로/대상/파일}}`

- 루트에 상대적인 경로에서 폴더 복구(경로를 `/`로 시작하지 마세요):

`extundelete {{/dev/sdXN}} --restore-directory {{경로/대상/폴더}}`

- 2020년 1월 1일 이후 삭제된 모든 파일 복구(Unix 시간 기준):

`extundelete {{/dev/sdXN}} --restore-all --after {{1577840400}}`
