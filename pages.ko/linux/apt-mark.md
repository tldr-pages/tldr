# apt-mark

> 설치된 패키지의 상태를 변경하는 유틸리티.
> 더 많은 정보: <https://manned.org/apt-mark.8>.

- 패키지를 자동 설치로 표시:

`sudo apt-mark auto {{패키지}}`

- 패키지를 현재 버전으로 고정하고 업데이트 방지:

`sudo apt-mark hold {{패키지}}`

- 패키지를 다시 업데이트 가능하도록 허용:

`sudo apt-mark unhold {{패키지}}`

- 수동으로 설치된 패키지 표시:

`apt-mark showmanual`

- 업데이트되지 않는 고정된 패키지 표시:

`apt-mark showhold`
