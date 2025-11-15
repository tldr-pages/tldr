# perl

> Perl 5 언어 인터프리터.
> 더 많은 정보: <https://perldoc.perl.org/perl>.

- `stdin`에서 regex1과 일치하고 대소문자를 구분하지 않는 regex2와 일치하는 행 출력:

`perl -n -e 'print if m/{{regex1}}/ and m/{{regex2}}/i'`

- 공백을 무시하고 정규식을 사용하여 첫 번째 매치 그룹 출력:

`perl -n -E 'say $1 if m/{{이전}} ( {{정규식_그룹}} ) {{이후}}/x'`

- 백업과 함께 제자리에서 모든 regex 발생을 대체:

`perl -i'.bak' -p -e 's/{{regex}}/{{대체}}/g' {{경로/대상/파일들}}`

- Perl의 인라인 문서 사용, 일부 페이지는 Linux의 매뉴얼 페이지에서도 사용 가능:

`perldoc perlrun ; perldoc module ; perldoc -f splice; perldoc -q perlfaq1`
