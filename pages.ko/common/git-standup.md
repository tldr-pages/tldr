# git standup

> 지정된 사용자의 커밋을 확인.
> `git-extras`의 일부.
> 더 많은 정보: <https://manned.org/git-standup>.

- 지정된 작성자의 최근 10일간의 커밋 보기:

`git standup -a {{이름|이메일}} -d {{10}}`

- 지정된 작성자의 최근 10일간의 커밋 및 GPG 서명 여부 확인:

`git standup -a {{이름|이메일}} -d {{10}} -g`

- 최근 10일간 모든 기여자의 모든 커밋 보기:

`git standup -a all -d {{10}}`

- 도움말 표시:

`git standup -h`
