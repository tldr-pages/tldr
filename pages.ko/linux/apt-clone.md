# apt-clone

> Debian 기반 시스템의 패키지 상태를 복제/백업/복원합니다.
> 더 많은 정보: <https://github.com/mvo5/apt-clone>.

- 현재 시스템의 패키지 상태를 지정한 디렉터리에 복제:

`apt-clone clone {{경로/대상/폴더}}`

- 백업 용도로 클론 파일 (`tar.gz`) 생성:

`apt-clone clone --destination {{경로/대상/백업.tar.gz}}`

- 클론 파일에서 패키지 상태 복원:

`apt-clone restore {{경로/대상/백업.tar.gz}}`

- 클론 파일에 대한 정보 표시 (예: 릴리스, 아키텍처):

`apt-clone info {{경로/대상/백업.tar.gz}}`

- 클론 파일을 현재 시스템에서 복원할 수 있는지 확인:

`apt-clone restore {{경로/대상/백업.tar.gz}} --destination {{경로/대상/복원}}`
