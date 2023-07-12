# base32

> 파일 또는 표준 입력을 Base32와 표준 출력으로 인코딩하거나 디코딩함.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/base32>.

- 파일 인코딩:

`base32 {{filename}}`

- 파일 디코딩:

`base32 --decode {{filename}}`

- `stdin`에서 인코딩:

`{{somecommand}} | base32`

- `stdin`에서 디코딩:

`{{somecommand}} | base32 --decode`
