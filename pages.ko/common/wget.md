# wget

> 웹에서 파일을 다운로드합니다.
> HTTP, HTTPS 및 FTP를 지원합니다.
> 더 많은 정보: <https://www.gnu.org/software/wget>.

- URL 내용을 파일(이 경우 "foo")로 다운로드:

`wget {{https://example.com/foo}}`

- URL 내용을 파일(이 경우 "bar")로 다운로드:

`wget --output-document {{bar}} {{https://example.com/foo}}`

- 요청 사이에 3초 간격으로 단일 웹 페이지와 모든 리소스(스크립트, 스타일시트, 이미지 등)를 다운로드:

`wget --page-requisites --convert-links --wait=3 {{https://example.com/somepage.html}}`

- 폴더 및 해당 폴더 내에 나열된 모든 파일을 다운로드(포함된 페이지는 다운로드하지 않음):

`wget --mirror --no-parent {{https://example.com/somepath/}}`

- 다운로드 속도와 연결 재시도 횟수를 제한:

`wget --limit-rate={{300k}} --tries={{100}} {{https://example.com/somepath/}}`

- 기본 인증을 사용하여 HTTP 서버에서 파일 다운로드(FTP에서도 작동):

`wget --user={{사용자 명}} --password={{비밀번호}} {{https://example.com}}`

- 불완전한 다운로드 계속 진행:

`wget --continue {{https://example.com}}`

- 텍스트 파일에 저장된 모든 URL을 특정 디렉토리로 다운로드:

`wget --directory-prefix {{경로/대상/폴더}} --input-file {{URLs.txt}}`
