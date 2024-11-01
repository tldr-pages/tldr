# xmlstarlet

> 명령줄 XML/XSLT 도구 모음.
> 참고: XPath를 알아야 할 수도 있습니다: <https://developer.mozilla.org/en-US/docs/Web/XPath>.
> 더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- XML 문서를 포맷하여 `stdout`에 출력:

`xmlstarlet format {{경로/대상/파일.xml}}`

- XML 문서를 `stdin`에서 파이프로 입력할 수도 있음:

`{{cat 경로/대상/파일.xml}} | xmlstarlet format`

- 주어진 XPath와 일치하는 모든 노드 출력:

`xmlstarlet select --template --copy-of {{xpath}} {{경로/대상/파일.xml}}`

- 일치하는 모든 노드에 속성을 삽입하고 `stdout`에 출력 (원본 파일은 변경되지 않음):

`xmlstarlet edit --insert {{xpath}} --type attr --name {{속성_이름}} --value {{속성_값}} {{경로/대상/파일.xml}}`

- 일치하는 모든 노드의 값을 직접 업데이트 (원본 파일이 변경됨):

`xmlstarlet edit --inplace --update {{xpath}} --value {{새로운_값}} {{파일.xml}}`

- 일치하는 모든 노드 삭제 (원본 파일이 변경됨):

`xmlstarlet edit --inplace --delete {{xpath}} {{파일.xml}}`

- 주어진 문자열의 특수 XML 문자를 이스케이프 또는 언이스케이프:

`xmlstarlet [un]escape {{문자열}}`

- 주어진 디렉토리를 XML로 나열 (인수를 생략하면 현재 디렉토리를 나열):

`xmlstarlet ls {{경로/대상/폴더}}`
