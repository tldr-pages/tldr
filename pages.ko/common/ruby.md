# ruby

> Ruby 프로그래밍 언어 인터프리터.
> 같이 보기: `gem`, `bundler`, `rake`, `irb`.
> 더 많은 정보: <https://manned.org/ruby>.

- Ruby 스크립트 실행:

`ruby {{스크립트.rb}}`

- 명령줄에서 단일 Ruby 명령 실행:

`ruby -e {{명령}}`

- 주어진 Ruby 스크립트에서 구문 오류 확인:

`ruby -c {{스크립트.rb}}`

- 현재 디렉토리에서 포트 8080으로 내장 HTTP 서버 시작:

`ruby -run -e httpd`

- 필요한 라이브러리를 설치하지 않고 로컬에서 Ruby 바이너리 실행:

`ruby -I {{라이브러리_폴더_경로}} -r {{라이브러리_요구_이름}} {{바이너리_폴더_경로/바이너리_이름}}`

- Ruby 버전 표시:

`ruby {{[-v|--version]}}`
