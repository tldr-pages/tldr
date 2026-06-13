# ident

> 파일 내 RCS 키워드 문자열을 식별.
> 관련 항목: `ci`, `co`, `rcs`, `rcsdiff`, `rlog`.
> 더 많은 정보: <https://manned.org/ident>.

- 파일에서 RCS 식별 문자열 출력:

`ident {{경로/대상/파일}}`

- 패턴이 없을 경우 경고를 표시하지 않고 RCS 식별 문자열 출력:

`ident -q {{경로/대상/파일1 경로/대상/파일2 ...}}`

- `stdin`으로부터 RCS 식별 문자열 출력:

`cat {{경로/대상/파일}} | ident`
