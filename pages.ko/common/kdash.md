# kdash

> Kubernetes용 간단한 대시보드.
> 더 많은 정보: <https://github.com/kdash-rs/kdash/#usage>.

- 대시보드 표시:

`kdash`

- 디버그 모드로 대시보드 실행하고 현재 디렉터리에 로그 파일 기록:

`kdash {{[-d|--debug]}}`

- tick rate 설정:

`kdash {{[-t|--tick-rate]}} {{100}}`

- polling rate 설정 (tick rate의 배수여야 함):

`kdash {{[-t|--tick-rate]}} {{200}} {{[-p|--poll-rate]}} {{400}}`
