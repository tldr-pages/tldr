# kerl

> Erlang/OTP 인스턴스를 쉽게 빌드 및 설치.
> 더 많은 정보: <https://github.com/kerl/kerl>.

- 특정 Erlang/OTP 버전을 디렉터리에 빌드 및 설치:

`kerl build-install {{28.0}} {{28.0}} {{경로/대상/설치_디렉토리}}/{{28.0}}`

- Erlang/OTP 설치 활성화:

`. {{경로/대상/설치}}/activate`

- 현재 활성화된 Erlang/OTP 설치 비활성화:

`kerl_deactivate`

- 사용 가능한 모든 Erlang/OTP 릴리스 목록 표시:

`kerl list releases`

- 설치된 Erlang/OTP 빌드 목록 표시:

`kerl list installations`
