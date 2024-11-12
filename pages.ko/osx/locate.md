# locate

> 파일명을 빠르게 찾습니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/locate.1.html>.

- 데이터베이스에서 패턴 검색 (참고: 데이터베이스는 주기적으로 다시 계산됩니다, 보통 주간 또는 일간):

`locate "{{패턴}}"`

- 파일명을 정확히 일치시켜 검색 (글로빙 문자가 없는 패턴은 `*패턴*`으로 해석됨):

`locate */{{파일명}}`

- 데이터베이스 다시 계산 (최근에 추가된 파일을 찾고자 할 경우 필요):

`sudo /usr/libexec/locate.updatedb`
