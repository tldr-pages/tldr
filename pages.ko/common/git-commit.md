# git commit

> 파일을 저장소에 커밋합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-commit>.

- 스테이징된 파일을 메시지와 함께 저장소에 커밋:

`git commit --message "{{메시지}}"`

- 파일에서 읽은 메시지로 스테이징된 파일을 저장소에 커밋:

`git commit --file {{파일/커밋_메시지_경로}}`

- 수정 및 삭제된 모든 파일을 자동으로 스테이징하고 메시지와 함께 커밋:

`git commit --all --message "{{메시지}}"`

- 스테이징된 파일을 커밋하고 지정된 GPG 키로 서명합니다 (인수가 지정되지 않은 경우 구성 파일에 정의된 키 사용):

`git commit --gpg-sign {{키_아이디}} --message "{{메시지}}"`

- 현재 스테이징된 변경 사항을 추가하여 마지막 커밋을 업데이트하고 커밋의 해시를 변경합니다:

`git commit --amend`

- 특정 파일(이미 스테이징된)만 커밋:

`git commit {{파일/경로1}} {{파일/경로2}}`

- 스테이징된 파일이 없더라도 커밋 생성:

`git commit --message "{{메시지}}" --allow-empty`
