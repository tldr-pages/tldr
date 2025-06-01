# xml canonic

> XML 문서를 정규화.
> 더 많은 정보: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139560880>.

- XML 문서를 정규화하여 주석을 보존:

`xml {{[c14n|canonic]}} {{경로/대상/입력.xml|URI}} > {{경로/대상/출력.xml}}`

- XML 문서를 정규화하여 주석 제거:

`xml {{[c14n|canonic]}} --without-comments {{경로/대상/입력.xml|URI}} > {{경로/대상/출력.xml}}`

- 파일의 XPATH를 사용하여 XML을 독점적으로 정규화하고, 주석을 보존:

`xml {{[c14n|canonic]}} --exc-with-comments {{경로/대상/입력.xml|URI}} {{경로/대상/c14n.xpath}}`

- 도움말 표시:

`xml {{[c14n|canonic]}} --help`
