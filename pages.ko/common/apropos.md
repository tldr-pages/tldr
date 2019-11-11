# apropos

> 메뉴얼 페이지에서 검색, 예를 들어 새로운 명령어 검색.

- 키워드 검색:

`apropos {{regular_expression}}`

- 출력을 터미널 너비에 제한을 두지 않고 검색:

`apropos -l {{regular_expression}}`

- 주어진 모든 표현식만 포함하는 페이지 검색(AND 검색):

`apropos {{regular_expression_1}} -a {{regular_expression_2}} -a {{regular_expression_3}`