# history

> 명령줄 히스토리를 관리.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-history>.

- 명령줄 히스토리를 줄 번호와 함께 출력:

`history`

- 최근 20개의 명령어 출력 (Zsh에서는 20번째 이후의 모든 명령어 출력):

`history 20`

- 다양한 형식의 타임스탬프와 함께 히스토리 출력 (Zsh 전용):

`history -{{d|f|i|E}}`

- 명령어 히스토리 목록 삭제([c]lear):

`history -c`

- 현재 Bash 쉘의 히스토리로 히스토리 파일을 덮어쓰기(Over[w]rite) (보통 `history -c`와 함께 사용하여 히스토리를 완전히 삭제할 때 사용):

`history -w`

- 지정한 위치(offset)의 히스토리 항목 삭제([d]elete):

`history -d {{오프셋}}`

- 명령어를 실행하지 않고 히스토리에 추가:

`history -s {{명령어}}`

- 명령어 앞에 공백을 추가하여 히스토리에 기록하지 않고 실행:

`<Space>{{명령어}}`
