# cdecl

> C 및 C++ 타입 선언을 작성하고 디코딩.
> 더 많은 정보: <https://manned.org/cdecl>.

- 영어 구문을 C 선언으로 작성하고, 컴파일 가능한([c]ompilable) 출력을 생성 (`;` 및 `{}` 포함):

`cdecl -c {{구문}}`

- C 선언을 영어로 설명:

`cdecl explain {{C_선언}}`

- 변수를 다른 타입으로 캐스팅:

`cdecl cast {{변수_이름}} to {{타입}}`

- 대화형([i]nteractive) 모드에서 실행:

`cdecl -i`
