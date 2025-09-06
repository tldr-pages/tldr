# mkhomedir_helper

> 사용자 생성 후 사용자의 홈 디렉토리를 만듭니다.
> 더 많은 정보: <https://manned.org/mkhomedir_helper>.

- umask 022로 `/etc/skel`을 기반으로 사용자 홈 디렉토리 생성:

`sudo mkhomedir_helper {{사용자명}}`

- 소유자에게 모든 권한(0)을, 그룹에게 읽기 권한(3)을 부여한 umask 037로 `/etc/skel`을 기반으로 사용자 홈 디렉토리 생성:

`sudo mkhomedir_helper {{사용자명}} {{037}}`

- 사용자 지정 스켈레톤을 기반으로 사용자 홈 디렉토리 생성:

`sudo mkhomedir_helper {{사용자명}} {{umask}} {{경로/대상/스켈레톤_폴더}}`
