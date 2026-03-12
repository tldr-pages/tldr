# ruby

> Ruby 프로그래밍 언어 인터프리터.
> 관련 항목: `gem`, `bundler`, `rake`, `irb`.
> 더 많은 정보: <https://manned.org/ruby>.

- Ruby 스크립트를 실행:

`ruby {{경로/대상/스크립트.rb}}`

- 명령줄에서 단일 Ruby 명령을 실행:

`ruby -e "{{명령어}}"`

- 지정한 Ruby 스크립트의 문법 오류를 확인:

`ruby -c {{경로/대상/스크립트.rb}}`

- 현재 디렉터리에서 내장 HTTP 서버를 포트 8080으로 실행:

`ruby -run -e httpd`

- 필요한 라이브러리를 설치하지 않고 로컬 Ruby 바이너리를 실행:

`ruby -I {{경로/대상/라이브러리_폴더}} -r {{require에_포함될_라이브러리_이름}} {{경로/대상/bin_폴더/bin_이름}}`

- 버전 정보 표시:

`ruby {{[-v|--version]}}`