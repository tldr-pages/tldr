# mktemp

> 임시 파일 또는 디렉터리 생성.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/mktemp.1.html>.

- 빈 임시 파일을 생성하고 절대 경로 출력:

`mktemp`

- 사용자 정의 디렉터리 사용 (`getconf DARWIN_USER_TEMP_DIR`의 출력 또는 `/tmp`가 기본값):

`mktemp --tmpdir {{/경로/대상/임시_폴더}}`

- 사용자 정의 경로 템플릿 사용 (`X`는 무작위 영숫자 문자로 대체됨):

`mktemp {{/tmp/example.XXXXXXXX}}`

- 사용자 정의 파일 이름 접두사 사용:

`mktemp -t {{예제}}`

- 빈 임시 디렉터리를 생성하고 절대 경로 출력:

`mktemp --directory`
