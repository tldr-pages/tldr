# fonttools subset

> 글꼴의 서브셋을 생성하거나 파일 크기를 최적화.
> 더 많은 정보: <https://fonttools.readthedocs.io/en/latest/subset/index.html>.

- TTF 글꼴 파일을 Basic Latin 유니코드 블록만 포함하도록 서브셋 생성:

`fonttools subset {{경로/대상/폰트.ttf}} --unicodes=U+0000-007F`

- 출력 파일 형식을 WOFF2로 변경:

`fonttools subset {{경로/대상/폰트.ttf}} --unicodes=U+0000-007F --flavor=woff2`

- OpenType 글꼴 기능 중 onum (oldstyle figures)과 kern (kerning)만 유지:

`fonttools subset {{경로/대상/폰트.ttf}} --unicodes=U+0000-007F --layout-features=onum,kern`

- 출력 파일 이름 지정:

`fonttools subset {{경로/대상/폰트.ttf}} --unicodes=U+0000-007F --output-file={{경로/대상/서브셋.ttf}}`
