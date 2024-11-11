# fcrackzip

> ZIP 압축 파일 비밀번호 크랙 도구.
> 더 많은 정보: <https://manned.org/fcrackzip>.

- 4에서 8자리의 길이를 가지며, 영숫자만 포함된 비밀번호를 무차별 대입으로 찾기 (순서 중요):

`fcrackzip --brute-force --length 4-8 --charset aA1 {{압축_파일}}`

- 자세히 보기 모드에서 3자리의 길이를 가지며, 소문자, `$` 및 `%`만 포함된 비밀번호를 무차별 대입으로 찾기:

`fcrackzip -v --brute-force --length 3 --charset a:$% {{압축_파일}}`

- 소문자와 특수 문자만 포함된 비밀번호를 무차별 대입으로 찾기:

`fcrackzip --brute-force --length 4 --charset a! {{압축_파일}}`

- 숫자만 포함된 비밀번호를 `12345`부터 시작하여 무차별 대입으로 찾기:

`fcrackzip --brute-force --length 5 --charset 1 --init-password 12345 {{압축_파일}}`

- 사전 목록을 사용하여 비밀번호 크랙:

`fcrackzip --use-unzip --dictionary --init-password {{단어목록}} {{압축_파일}}`

- 크랙 성능 벤치마크:

`fcrackzip --benchmark`
