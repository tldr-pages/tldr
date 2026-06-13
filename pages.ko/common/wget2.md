# wget2

> 웹에서 파일을 다운로드하기 위한 개선된 `wget` 버전.
> HTTP, HTTPS 및 HTTP/2 프로토콜을 지원하며 성능이 향상되었습니다.
> 기본적으로 `wget2`는 더 빠른 다운로드를 위해 여러 스레드를 사용합니다.
> 더 많은 정보: <https://manned.org/wget2>.

- 여러 스레드를 사용하여 URL의 내용을 파일로 다운로드 (기본 동작이 `wget`과 다릅니다):

`wget2 {{https://example.com/foo}}`

- 다운로드에 사용할 스레드 수 제한 (기본값은 5 스레드):

`wget2 --max-threads {{10}} {{https://example.com/foo}}`

- 단일 웹 페이지와 모든 리소스(스크립트, 스타일시트, 이미지 등) 다운로드:

`wget2 {{[-p|--page-requisites]}} {{[-k|--convert-links]}} {{https://example.com/somepage.html}}`

- 웹사이트를 미러링하되 상위 디렉토리로 올라가지 않음 (내장 페이지 요소는 다운로드하지 않음):

`wget2 {{[-m|--mirror]}} {{[-np|--no-parent]}} {{https://example.com/somepath/}}`

- 다운로드 속도와 연결 재시도 횟수 제한:

`wget2 --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/somepath/}}`

- 불완전한 다운로드 계속 (동작이 `wget`과 일치):

`wget2 {{[-c|--continue]}} {{https://example.com}}`

- 텍스트 파일에 저장된 모든 URL을 특정 디렉토리에 다운로드:

`wget2 {{[-P|--directory-prefix]}} {{경로/대상/폴더}} {{[-i|--input-file]}} {{URLs.txt}}`

- HTTP 서버에서 Basic Auth를 사용하여 파일 다운로드 (HTTPS에도 작동):

`wget2 --user {{사용자_명}} --password {{비밀번호}} {{https://example.com}}`
