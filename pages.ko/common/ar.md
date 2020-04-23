# ar

> 아카이브로부터 생성, 수정, 추출 (.a, .so, .o).

- 보관소로부터 모든 멤버를 추출하기:

`ar -x {{libfoo.a}}`

- 보관소 멤버 리스트 보여주기:

`ar -t {{libfoo.a}}`

- 보관소로 파일을 대체하거나 추가하기:

`ar -r {{libfoo.a}} {{foo.o}} {{bar.o}} {{baz.o}}`

- object 파일 인덱스 삽입( `ranlib` 와 같은 기능입니다):

`ar -s {{libfoo.a}}`

- 파일 및 첨부된 객체 파일 색인을 사용하여 보관소에 작성:

`ar -rs {{libfoo.a}} {{foo.o}} {{bar.o}} {{baz.o}}`
