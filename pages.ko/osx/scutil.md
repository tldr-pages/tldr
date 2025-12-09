# scutil

> 시스템 구성 매개변수를 관리합니다.
> 구성 설정 시 루트 권한이 필요합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/scutil.8.html>.

- DNS 구성 표시:

`scutil --dns`

- 프록시 구성 표시:

`scutil --proxy`

- 컴퓨터 이름 확인:

`scutil --get ComputerName`

- 컴퓨터 이름 설정:

`sudo scutil --set ComputerName {{컴퓨터_이름}}`

- 호스트명 확인:

`scutil --get HostName`

- 호스트명 설정:

`scutil --set HostName {{호스트명}}`
