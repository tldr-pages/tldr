# history

> 커멘드 라인 히스토리.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-history>.

- 줄 번호와 함께 명령 기록 목록을 표시:

`history`

- 마지막 20개의 명령을 표시 (Zsh에서는 20번째부터 시작하는 모든 명령을 표시):

`history {{20}}`

- 다양한 형식의 타임스탬프가 포함된 기록을 표시 (Zsh에서만 사용 가능):

`history -{{d|f|i|E}}`

- 명령 기록 목록을 삭제([c]lear) (현재 Bash 쉘에만 해당):

`history -c`

- 현재 Bash 쉘의 기록으로 기록 파일 덮어쓰기(Over[w]rite) (종종 기록을 제거하기 위해 `history -c`와 결합되어 사용):

`history -w`

- 지정된 오프셋에서 기록 항목을 삭제([d]elete):

`history -d {{오프셋}}`
