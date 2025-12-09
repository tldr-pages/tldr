# tic

> terminfo를 컴파일하고 ncurses에 설치합니다.
> 더 많은 정보: <https://manned.org/tic>.

- 터미널에 대한 terminfo를 컴파일하고 설치:

`tic -xe {{터미널}} {{경로/대상/터미널.info}}`

- terminfo 파일의 오류 확인:

`tic -c {{경로/대상/터미널.info}}`

- 데이터베이스 위치 출력:

`tic -D`
