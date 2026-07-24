# fonttools

> Python에서 글꼴을 조작하는 도구.
> 더 많은 정보: <https://fonttools.readthedocs.io/en/latest/>.

- TTF 글꼴 파일을 Basic Latin 유니코드 블록만 포함하도록 서브셋 생성:

`fonttools subset {{path/to/font.ttf}} --unicodes=U+0000-007F`

- 도움말 표시:

`fonttools --help`
