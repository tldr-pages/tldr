# ddev

> PHP 환경을 위한 컨테이너 기반 로컬 개발도구.
> 더 많은 정보: <https://ddev.readthedocs.io/en/stable/users/usage/cli/>.

- 프로젝트 시작:

`ddev start`

- 프로젝트 유형 및 문서 루트를 구성:

`ddev config`

- 로그를 계속해서 출력([f]ollow):

`ddev logs -f`

- 컨테이너 내에서 composer를 실행:

`ddev composer`

- 특정 Node.js 버전 설치:

`ddev nvm install {{버전}}`

- 데이터베이스 내보내기:

`ddev export-db --file={{/tmp/db.sql.gz}}`

- 컨테이너 내에서 특정 명령을 실행:

`ddev exec {{echo 1}}`
