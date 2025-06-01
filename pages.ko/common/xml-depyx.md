# xml depyx

> PYX (ESIS - ISO 8879) 문서를 XML 형식으로 변환.
> 더 많은 정보: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139550832>.

- PYX (ESIS - ISO 8879) 문서를 XML 형식으로 변환:

`xml {{[p2x|depyx]}} {{경로/대상/입력.pyx|URI}} > {{경로/대상/출력.xml}}`

- `stdin`에서 PYX 문서를 XML 형식으로 변환:

`cat {{경로/대상/입력.pyx}} | xml {{[p2x|depyx]}} > {{경로/대상/출력.xml}}`

- 도움말 표시:

`xml {{[p2x|depyx]}} --help`
