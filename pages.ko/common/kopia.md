# kopia

> 빠르고 안전한 오픈 소스 백업 도구.
> 암호화, 압축, 중복 제거 및 증분 스냅샷을 지원합니다.
> 더 많은 정보: <https://kopia.io/docs/reference/command-line/>.

- 로컬 파일 시스템에 저장소 생성:

`kopia repository create filesystem --path {{경로/대상/로컬_저장소}}`

- Amazon S3에 저장소 생성:

`kopia repository create s3 --bucket {{버킷_이름}} --access-key {{AWS_액세스_키_ID}} --secret-access-key {{AWS_비밀_액세스_키}}`

- 저장소에 연결:

`kopia repository connect {{저장소_유형}} --path {{경로/대상/저장소}}`

- 디렉터리의 스냅샷 생성:

`kopia snapshot create {{경로/대상/폴더}}`

- 스냅샷 나열:

`kopia snapshot list`

- 특정 디렉터리에 스냅샷 복원:

`kopia snapshot restore {{스냅샷_ID}} {{경로/대상/목표_폴더}}`

- 새 정책 생성:

`kopia policy set --global --keep-latest {{유지할_스냅샷_수}} --compression {{압축_알고리즘}}`

- 특정 파일 또는 폴더를 백업에서 제외:

`kopia policy set --global --add-ignore {{경로/대상/파일_또는_폴더}}`
