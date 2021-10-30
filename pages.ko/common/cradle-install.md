# cradle install

> Cradle PHP 프레임워크 구성 요소를 설치.
> 더 많은 정보: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>.

- Cradle의 구성요소 설치 (유저는 자세한 내용을 묻는 메시지를 받음):

`cradle install`

- 파일을 강제로 덮어 쓰기:

`cradle install --force`

- 실행중인 SQL 마이그레이션 건너 뛰기:

`cradle install --skip-sql`

- 실행중인 패키지 업데이트 건너 뛰기:

`cradle install --skip-versioning`

- 특정 데이터베이스 세부 사항 사용:

`cradle install -h {{호스트명}} -u {{유저명}} -p {{비밀번호}}`
