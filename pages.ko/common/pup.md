# pup

> 명령줄 HTML 파싱 도구.
> 더 많은 정보: <https://github.com/ericchiang/pup>.

- 원시 HTML 파일을 정리되고 들여쓰기된 색상 형식으로 변환:

`cat {{index.html}} | pup --color`

- 요소 태그 이름으로 HTML 필터링:

`cat {{index.html}} | pup '{{태그}}'`

- ID로 HTML 필터링:

`cat {{index.html}} | pup '{{div#아이디}}'`

- 속성 값으로 HTML 필터링:

`cat {{index.html}} | pup '{{input[type="text"]}}'`

- 필터링된 HTML 요소와 그 자식 요소의 모든 텍스트 출력:

`cat {{index.html}} | pup '{{div}} text{}'`

- HTML을 JSON으로 출력:

`cat {{index.html}} | pup '{{div}} json{}'`
