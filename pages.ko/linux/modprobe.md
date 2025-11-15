# modprobe

> Linux 커널에 모듈을 추가하거나 제거합니다.
> 더 많은 정보: <https://manned.org/modprobe>.

- 모듈을 커널에 로드하는 것처럼 시뮬레이션하지만 실제로는 하지 않음:

`sudo modprobe --dry-run {{모듈_이름}}`

- 모듈을 커널에 로드:

`sudo modprobe {{모듈_이름}}`

- 모듈을 커널에서 제거:

`sudo modprobe --remove {{모듈_이름}}`

- 모듈과 해당 모듈에 의존하는 모듈을 커널에서 제거:

`sudo modprobe {{[-r|--remove]}} --remove-holders {{모듈_이름}}`

- 커널 모듈의 의존성 표시:

`sudo modprobe --show-depends {{모듈_이름}}`
