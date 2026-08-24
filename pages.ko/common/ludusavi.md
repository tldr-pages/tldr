# ludusavi

> 비디오 게임 저장 데이터 백업 도구.
> 더 많은 정보: <https://github.com/mtkennerly/ludusavi/blob/master/docs/cli.md>.

- 게임 저장 데이터 백업:

`ludusavi backup --path {{경로/대상/백업}}`

- 게임 저장 데이터 복원:

`ludusavi restore --path {{경로/대상/백업}} {{"게임1" "게임2" ...}}`

- 백업 목록 조회:

`ludusavi backups --path {{경로/대상/백업}}`

- 게임 런처와 연동하여 실행 전후 자동 백업/복원 수행:

`ludusavi wrap --gui --infer {{heroic|lutris|steam}} -- {{게임_실행_명령어}}`

- 독립 실행형 게임을 감싸서 자동 백업/복원 수행:

`ludusavi wrap --gui --name {{이름}} -- {{게임_실행_명령어}}`
