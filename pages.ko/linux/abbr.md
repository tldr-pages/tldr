# abbr

> fish 쉘에서 약어를 관리합니다.
> 사용자 정의 단어는 입력 후 더 긴 구문으로 대체됩니다.
> 더 많은 정보: <https://fishshell.com/docs/current/cmds/abbr.html>.

- 새 약어 추가:

`abbr --add {{약어_이름}} {{명령어}} {{명령어_인수}}`

- 기존 약어 이름 변경:

`abbr --rename {{기존_이름}} {{새로운_이름}}`

- 기존 약어 삭제:

`abbr --erase {{약어_이름}}`

- SSH를 통해 다른 호스트의 약어 가져오기:

`ssh {{호스트_이름}} abbr --show | source`
