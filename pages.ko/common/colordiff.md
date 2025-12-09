# colordiff

> 동일한 출력을 생성하지만, 구문 강조가 잘 되어있는 `diff` 래퍼입니다.
> 색깔 구성표를 사용자 정의할 수 있음.
> 더 많은 정보: <https://github.com/kimmel/colordiff>.

- 파일 비교:

`colordiff {{파일1}} {{파일2}}`

- 두 개의 열로 출력:

`colordiff -y {{파일1}} {{파일2}}`

- 파일 내용의 대소문자 차이를 무시:

`colordiff -i {{파일1}} {{파일2}}`

- 두 파일이 동일한 경우에 보고:

`colordiff -s {{파일1}} {{파일2}}`

- 공백을 무시:

`colordiff -w {{파일1}} {{파일2}}`
