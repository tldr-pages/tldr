# distccd

> distcc 분산 컴파일러용 서버 데몬.
> 더 많은 정보: <https://distcc.github.io>.

- 기본 설정으로 데몬을 시작:

`distccd --daemon`

- IPv4 개인 네트워크 범위 연결을 수락해 데몬을 시작:

`distccd --daemon --allow-private`

- 특정 네트워크 주소 또는 주소 버위로부터의 연결을 수락해 데몬을 시작:

`distccd --daemon --allow {{ip_주소|네트워크_접두사}}`

- 한 번에 최대 4개의 작업을 실행할 수 있는 낮은 우선순위로 데몬을 시작:

`distccd --daemon --jobs {{4}} --nice {{5}}`

- 데몬을 시작하고 mDNS/DNS-SD (Zeroconf)를 통해 등록:

`distccd --daemon --zeroconf`
