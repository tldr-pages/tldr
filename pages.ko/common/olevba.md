# olevba

> Parse OLE 및 OpenXML 파일 (DOC, XLS, PPT 등)을 분석해 VBA 매크로를 추출하고, 난독화를 해제하며, 악성코드를 분석.
> `python-oletools` 제품군의 일분.
> 더 많은 정보: <https://github.com/decalage2/oletools>.

- 파일을 분석하여, 매크로 코드와 분석 결과를 함께 표시:

`olevba {{경로/대상/파일}}`

- 디렉터리 내 지원되는 모든 파일을 재귀적으로 분석:

`olevba -r {{경로/대상/디렉터리}}`

- 암호화된 Microsoft Office 파일의 비밀번호 지정 (여러 번 지정 가능):

`olevba {{[-p|--password]}} {{비밀번호}} {{경로/대상/암호화된_파일}}`

- 매크로 소스 코드를 제외한 분석 결과만 표시:

`olevba {{[-a|--analysis]}} {{경로/대상/파일}}`

- 매크로 소스 코드만 표시:

`olevba {{[-c|--code]}} {{경로/대상/파일}}`

- 난독화된 문자열과 복호화된 내용을 표시:

`olevba --decode {{경로/대상/파일}}`
