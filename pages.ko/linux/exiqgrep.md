# exiqgrep

> Exim 큐 출력에서 `grep`의 기능을 제공하는 Perl 스크립트.
> 더 많은 정보: <https://www.exim.org/exim-html-current/doc/html/spec_html/ch-exim_utilities.html>.

- 발신자 주소를 대소문자 구분 없이 검색:

`exiqgrep -f '<{{email@somedomain.com}}>'`

- 발신자 주소를 검색하고 메시지 ID만 표시:

`exiqgrep -i -f '<{{email@somedomain.com}}>'`

- 수신자 주소 검색:

`exiqgrep -r '{{email@somedomain.com}}'`

- 큐에서 발신자 주소와 일치하는 모든 메시지 제거:

`exiqgrep -i -f '<{{email@somedomain.com}}>' | xargs exim -Mrm`

- 반송된 메시지 테스트:

`exiqgrep -f '^<>$'`

- 반송된 메시지 개수 표시:

`exiqgrep -c -f '^<>$'`
