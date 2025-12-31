# xml validate

> XML 문서 유효성 검사.
> 더 많은 정보: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139576400>.

- 하나 이상의 XML 문서가 잘 형성되었는지 검사:

`xml {{[val|validate]}} {{경로/대상/입력1.xml|URI1 경로/대상/입력2.xml|URI2 ...}}`

- 하나 이상의 XML 문서를 문서 유형 정의(DTD)와 비교하여 유효성 검사:

`xml {{[val|validate]}} {{[-d|--dtd]}} {{경로/대상/스키마.dtd}} {{경로/대상/입력1.xml|URI1 경로/대상/입력2.xml|URI2 ...}}`

- 하나 이상의 XML 문서를 XML 스키마 정의(XSD)와 비교하여 유효성 검사:

`xml {{[val|validate]}} {{[-s|--xsd]}} {{경로/대상/스키마.xsd}} {{경로/대상/입력1.xml|URI1 경로/대상/입력2.xml|URI2 ...}}`

- 하나 이상의 XML 문서를 Relax NG 스키마(RNG)와 비교하여 유효성 검사:

`xml {{[val|validate]}} {{[-r|--relaxng]}} {{경로/대상/스키마.rng}} {{경로/대상/입력1.xml|URI1 경로/대상/입력2.xml|URI2 ...}}`

- 도움말 표시:

`xml {{[val|validate]}} --help`
