# comby

> 다양한 언어를 지원하는 구조적인 코드 검색 및 교체 도구.
> 더 많은 정보: <https://github.com/comby-tools/comby>.

- 템플릿 일치 및 재작성, 변경 사항 출력:

`comby '{{assert_eq!(:[a], :[b])}}' '{{assert_eq!(:[b], :[a])}}' {{.rs}}`

- 일치되는 부분을 찾고, 프로퍼티에 따른 교체를 수행:

`comby '{{assert_eq!(:[a], :[b])}}' '{{assert_eq!(:[b].Capitalize, :[a])}}' {{.rs}}`

- 패턴과 일치하는 부분을 찾고 바로 교체:

`comby -in-place '{{일치_패턴}}' '{{교체_패턴}}'`

- 패턴 검색만 수행하고 일치되는 항목을 출력:

`comby -match-only '{{일치_패턴}}' ""`
