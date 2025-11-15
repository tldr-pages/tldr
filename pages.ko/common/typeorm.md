# typeorm

> Node.js, 브라우저, Cordova, Ionic, React Native, NativeScript, Electron 플랫폼에서 실행할 수 있는 JavaScript ORM.
> 더 많은 정보: <https://typeorm.io/docs/advanced-topics/using-cli/#initialize-a-new-typeorm-project>.

- 새로운 TypeORM 프로젝트 구조 생성:

`typeorm init`

- 빈 마이그레이션 파일 생성:

`typeorm migration:create --name {{마이그레이션_이름}}`

- 스키마를 업데이트하는 SQL 문이 포함된 마이그레이션 파일 생성:

`typeorm migration:generate --name {{마이그레이션_이름}}`

- 대기 중인 모든 마이그레이션 실행:

`typeorm migration:run`

- 특정 디렉터리에 새 엔터티 파일 생성:

`typeorm entity:create --name {{엔터티}} --dir {{경로/대상/폴더}}`

- 기본 연결에서 `typeorm schema:sync`로 실행될 SQL 문 표시:

`typeorm schema:log`

- 기본 연결에서 특정 SQL 문 실행:

`typeorm query {{sql_문장}}`

- 하위 명령에 대한 도움말 표시:

`typeorm {{하위_명령}} --help`
