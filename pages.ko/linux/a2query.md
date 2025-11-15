# a2query

> Debian 기반 OS에서 Apache의 런타임 설정을 검색.
> 더 많은 정보: <https://manned.org/a2query>.

- 활성화된 Apache 모듈 나열:

`sudo a2query -m`

- 특정 모듈이 설치되어 있는지 확인:

`sudo a2query -m {{모듈_이름}}`

- 활성화된 가상 호스트 나열:

`sudo a2query -s`

- 현재 활성화된 멀티 프로세싱 모듈 표시:

`sudo a2query -M`

- Apache 버전 표시:

`sudo a2query -v`
