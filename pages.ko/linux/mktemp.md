# mktemp

> 임시 파일 또는 디렉토리 생성.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/mktemp-invocation.html>.

- 빈 임시 파일을 생성하고 절대 경로 출력:

`mktemp`

- 사용자 지정 디렉토리 사용 (기본값: `$TMPDIR`, 또는 `/tmp`):

`mktemp {{[-p |--tmpdir=]}}{{/경로/대상/tempdir}}`

- 사용자 지정 경로 템플릿 사용 (`X`는 무작위 영숫자 문자로 대체됨):

`mktemp {{/tmp/example.XXXXXXXX}}`

- 사용자 지정 파일명 템플릿 사용:

`mktemp -t {{example.XXXXXXXX}}`

- 주어진 접미사를 가진 빈 임시 파일을 생성하고 절대 경로 출력:

`mktemp --suffix {{.ext}}`

- 빈 임시 디렉토리를 생성하고 절대 경로 출력:

`mktemp {{[-d|--directory]}}`
