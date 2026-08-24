# gnugo

> 명령줄에서 바둑(Go) 플레이.
> 더 많은 정보: <https://www.gnu.org/software/gnugo/gnugo_3.html>.

- 대화형 바둑 게임 시작:

`gnugo`

- [대화형] 게임 중 J열 5행 위치에 돌 놓기:

`J5`

- 접바둑(handicap) 5점과 레벨 5 상대를 사용하여 게임 시작:

`gnugo --handicap 5 --level 5`

- 특정 파일의 123번째 수부터 게임 재개:

`gnugo {{[-l|--infile]}} {{경로/대상/게임.sgf}} {{[-L|--until]}} 123`

- 현재 바둑판 판세의 대략적인 점수 추정:

`gnugo --score estimate {{[-l|--infile]}} {{경로/대상/게임.sgf}}`
