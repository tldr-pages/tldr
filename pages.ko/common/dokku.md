# dokku

> 도커로 구동되는 미니-Heroku (PaaS).
> 하나의 `git-push` 명령을 사용하여 여러 언어로 다른 앱을 쉽게 배포 할수 있습니다.
> 더 많은 정보: <https://github.com/dokku/dokku>.

- 실행중인 앱들 목록보기:

`dokku apps`

- 앱 생성하기:

`dokku apps:create {{앱_이름}}`

- 앱 제거하기:

`dokku apps:destroy {{앱_이름}}`

- 플러그인 설치하기:

`dokku plugin:install {{전체_폴더_경로}}`

- 앱에 데이터베이스 연결하기:

`dokku {{db}}:link {{데이터베이스_이름}} {{앱_이름}}`
