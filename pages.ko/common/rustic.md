# rustic

> 빠르고 암호화된 중복 제거 백업을 Rust로 생성.
> 더 많은 정보: <https://github.com/rustic-rs/rustic>.

- 새 저장소 초기화:

`rustic init --repository {{/srv/rustic-repo}}`

- 파일/디렉토리의 새 백업을 저장소에 생성:

`rustic backup --repository {{/srv/rustic-repo}} {{경로/대상/파일_또는_폴더}}`
