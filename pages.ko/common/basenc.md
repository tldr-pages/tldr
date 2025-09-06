# basenc

> 지정된 인코딩을 사용하여 파일 또는 `stdin`을 `stdout`으로 인코딩하거나 디코딩함.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/basenc-invocation.html>.

- base64 인코딩으로 파일을 인코딩:

`basenc --base64 {{경로/대상/파일}}`

- base64 인코딩으로 파일을 디코딩:

`basenc --decode --base64 {{경로/대상/파일}}`

- 42개의 열이 있는 base32 인코딩을 사용하여 `stdin`에서 인코딩:

`{{명령어}} | basenc --base32 -w42`

- base32 인코딩을 사용하여 `stdin`에서 인코딩:

`{{명령어}} | basenc --base32`
