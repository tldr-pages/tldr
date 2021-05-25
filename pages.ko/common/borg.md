# borg

> 중복제거 백업 도구. 파일시스템으로 마운트할 수 있는 로컬 또는 원격 저장소를 제작.
> 더 많은 정보: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- (로컬) 저장소 초기화:

`borg init {{/저장소_디렉토리/의/경로}}`

- 디렉토리를 저장소에 백업하여, "Monday"라는 아카이브 생성:

`borg create --progress {{/저장소_디렉토리/의/경로}}::{{Monday}} {{/소스_디렉토리/의/경로}}`

- 저장소의 모든 아카이브 나열:

`borg list {{/저장소_디렉토리/의/경로}}`

- *.ext 파일을 제외하고 원격 저장소의 "Monday" 아카이브에서 특정 디렉토리 추출:

`borg extract {{user}}@{{host}}:{{/저장소_디렉토리/의/경로}}::{{Monday}} {{/타겟_디렉토리/의/경로}} --exclude '{{*.ext}}'`

- 7일이 지난 아카이브를 모두 삭제하고, 변경 사항을 나열하여 저장소 정리:

`borg prune --keep-within {{7d}} --list {{/저장소_디렉토리/의/경로}}`

- 저장소를 FUSE 파일 시스템으로 마운트:

`borg mount {{/저장소_디렉토리/의/경로}}::{{Monday}} {{/마운트포인트/의/경로}}`

- 아카이브 작성에 대한 도움말 표시:

`borg create --help`
