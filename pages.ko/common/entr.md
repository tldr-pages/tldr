# entr

> 파일이 변경되면 임의의 명령을 실행.
> 더 많은 정보: <https://eradman.com/entrproject/>.

- 하위 디렉터리의 파일이 변경되면 `make`로 다시 빌드:

`{{ag -l}} | entr {{make}}`

- 현재 디렉터리에 `.c` 소스 파일이 변경되면 `make`로 다시 빌드하고 테스트:

`{{ls *.c}} | entr {{'make && make test'}}`

- `ruby main.rb`를 실행하기 전에 이전에 생성된 ruby 하위 프로세스에 `SIGTERM`을 보냄:

`{{ls *.rb}} | entr -r {{ruby main.rb}}`

- 변경된 파일 (`/_`)을 인수로 사용하여 명령을 실행:

`{{ls *.sql}} | entr {{psql -f}} /_`

- 화면을 지우고([c]lear) SQL 스크립트가 업데이트된 후 쿼리를 실행:

`{{echo my.sql}} | entr -cp {{psql -f}} /_`

- 소스 파일이 변경되면 프로젝트를 다시 빌드하고, 출력을 처음 몇 줄로 제한:

`{{find src/}} | entr -s {{'make | sed 10q'}}`

- Node.js 서버를 시작하고 자동으로 로드(auto-[r]eload):

`{{ls *.js}} | entr -r {{node app.js}}`
