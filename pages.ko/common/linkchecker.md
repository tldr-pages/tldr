# linkchecker

> HTML 문서 및 웹사이트의 깨진 링크를 확인하는 명령줄 클라이언트.
> 더 많은 정보: <https://linkchecker.github.io/linkchecker/man/linkchecker.html>.

- <https://example.com/>에서 깨진 링크 찾기:

`linkchecker {{https://example.com/}}`

- 외부 도메인을 가리키는 URL도 확인:

`linkchecker --check-extern {{https://example.com/}}`

- 특정 정규 표현식과 일치하는 URL 무시:

`linkchecker --ignore-url {{정규_표현식}} {{https://example.com/}}`

- 결과를 CSV 파일로 출력:

`linkchecker --file-output {{csv}}/{{경로/대상/파일}} {{https://example.com/}}`
