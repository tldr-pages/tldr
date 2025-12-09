# gitmoji

> 커밋 시 이모티콘을 사용하기 위한 대화형 명령줄 도구입니다.
> 더 많은 정보: <https://github.com/carloscuesta/gitmoji-cli>.

- 커밋 마법사 시작:

`gitmoji --commit`

- git 훅을 초기화 (따라서, `git commit`이 실행될 때마다 `gitmoji`가 실행됨):

`gitmoji --init`

- git 훅을 제거:

`gitmoji --remove`

- 사용 가능한 모든 이모티콘과 설명을 나열:

`gitmoji --list`

- 키워드 목록에 대한 이모티콘 목록 검색:

`gitmoji --search {{키워드1}} {{키워드2}}`

- 기본 저장소에서 캐시된 이모티콘 목록 갱신:

`gitmoji --update`

- 전역 기본 설정 구성:

`gitmoji --config`
