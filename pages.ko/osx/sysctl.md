# sysctl

> 커널 상태 정보를 확인합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/sysctl.8.html>.

- 사용 가능한 모든 변수와 값 표시:

`sysctl -a`

- Apple 모델 식별자 표시:

`sysctl -n hw.model`

- CPU 모델 표시:

`sysctl -n machdep.cpu.brand_string`

- 사용 가능한 CPU 기능(MMX, SSE, SSE2, SSE3, AES 등) 표시:

`sysctl -n machdep.cpu.features`

- 변경 가능한 커널 상태 변수 설정:

`sysctl -w {{section.tunable}}={{값}}`
