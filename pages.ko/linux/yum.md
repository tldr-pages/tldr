# yum

> RHEL, Fedora, CentOS(이전 버전용)를 위한 패키지 관리 도구.
> 다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> 더 많은 정보: <https://manned.org/yum>.

- 새 패키지 설치:

`yum install {{패키지}}`

- 새 패키지를 설치하고 모든 질문에 대해 예로 가정 (업데이트에도 작동하며, 자동화된 업데이트에 유용):

`yum -y install {{패키지}}`

- 특정 명령을 제공하는 패키지 찾기:

`yum provides {{명령}}`

- 패키지 제거:

`yum remove {{패키지}}`

- 설치된 패키지에 대한 사용 가능한 업데이트 표시:

`yum check-update`

- 설치된 패키지를 최신 버전으로 업그레이드:

`yum upgrade`
