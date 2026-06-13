# caller

> 함수 호출 컨텍스트를 출력.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-caller>.

- 현재 함수가 호출된 줄 번호와 파일 이름을 출력:

`caller`

- 현재 함수가 호출된 줄 번호, 함수 이름, 파일 이름을 출력:

`caller 0`

- 현재 함수 호출 스택에서 `n` 프레임 이전의 줄 번호, 함수 이름, 파일 이름을 출력:

`caller {{n}}`
