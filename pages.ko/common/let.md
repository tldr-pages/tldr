# let

> 쉘에서 산술 표현식 계산.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-let>.

- 간단한 산술 표현식 계산:

`let "{{result = a + b}}"`

- 표현식에서 후위 증가 연산자와 대입 연산을 사용:

`let "{{x++}}"`

- 표현식 내 삼항 연산자 사용:

`let "{{result = (x > 10) ? x : 0}}"`

- 도움말 표시:

`let --help`
