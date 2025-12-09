# gitlab-runner

> GitLab 실행기 관리.
> 더 많은 정보: <https://docs.gitlab.com/runner/>.

- 실행기 등록:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{토큰}} --name {{이름}}`

- Docker 실행기로 실행기를 등록:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{토큰}} --name {{이름}} --executor {{docker}}`

- 실행기 등록 해제:

`sudo gitlab-runner unregister --name {{이름}}`

- 실행기 서비스 상태를 표시:

`sudo gitlab-runner status`

- 실행기 서비스를 다시 시작:

`sudo gitlab-runner restart`

- 등록된 실행기가 GitLab에 연결할 수 있는지 확인:

`sudo gitlab-runner verify`
