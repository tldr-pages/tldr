# docker login

> Docker 레지스트리에 로그인.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/login/>.

- 레지스트리에 대화형으로 로그인:

`docker login`

- 특정 사용자 명으로 레지스트리에 로그인 (사용자는 비밀번호를 입력하라는 메시지를 받음):

`docker login {{[-u|--username]}} {{사용자_명}}`

- 사용자 명과 비밀번호로 레지스트리에 로그인:

`docker login {{[-u|--username]}} {{사용자_명}} {{[-p|--password]}} {{비밀번호}} {{서버}}`

- `stdin`에서 비밀번호를 받아 레지스트리에 로그인:

`echo "{{비밀번호}}" | docker login {{[-u|--username]}} {{사용자_명}} --password-stdin`
