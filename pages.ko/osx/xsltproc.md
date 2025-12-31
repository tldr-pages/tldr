# xsltproc

> XSLT를 사용하여 XML을 변환하여 출력(주로 HTML 또는 XML)을 생성합니다.
> 더 많은 정보: <https://manned.org/xsltproc>.

- 특정 XSLT 스타일시트를 사용하여 XML 파일 변환:

`xsltproc --output {{경로/대상/출력_파일.html}} {{경로/대상/스타일시트_파일.xslt}} {{경로/대상/파일.xml}}`

- 스타일시트의 매개변수에 값을 전달:

`xsltproc --output {{경로/대상/출력_파일.html}} --stringparam "{{이름}}" "{{값}}" {{경로/대상/스타일시트_파일.xslt}} {{경로/대상/xml_파일.xml}}`
