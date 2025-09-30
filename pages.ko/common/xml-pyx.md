# xml pyx

> XML 문서를 PYX (ESIS - ISO 8879) 형식으로 변환.
> 더 많은 정보: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139550832>.

- XML 문서를 PYX 형식으로 변환:

`xml pyx {{경로/대상/입력.xml|URI}} > {{경로/대상/출력.pyx}}`

- `stdin`에서 XML 문서를 받아 PYX 형식으로 변환:

`cat {{경로/대상/입력.xml}} | xml pyx > {{경로/대상/출력.pyx}}`

- 도움말 표시:

`xml pyx --help`
