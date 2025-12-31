# urpmf

> 파일을 패키지에서 찾고 Mageia에서 해당 정보를 조회.
> 같이 보기: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmi.update`, `urpmq`.
> 더 많은 정보: <https://man.linuxreviews.org/man8/urpmf.8.html>.

- 파일을 포함하는 패키지 검색:

`urpmf {{파일명}}`

- 요약에 특정 키워드 [a]그리고 다른 키워드를 모두 포함하는 패키지 검색:

`urpmf --summary {{키워드1}} -a {{키워드2}}`

- 설명에 특정 키워드 [o]또는 다른 키워드를 포함하는 패키지 검색:

`urpmf --description {{키워드1}} -o {{키워드2}}`

- 이름에 특정 키워드를 대소문자 구분 없이 포함하지 않는 패키지를 ":" 대신 "|"를 [F]ield 구분자로 사용하여 검색:

`urpmf --description ! {{키워드}} -F'|'`
