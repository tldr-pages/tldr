# dkms

> 커널 모듈의 동적 빌드를 위한 프레임워크.
> 더 많은 정보: <https://manned.org/dkms>.

- 현재 설치된 모듈 나열:

`dkms status`

- 현재 실행 중인 커널에 대해 모든 모듈 다시 빌드:

`dkms autoinstall`

- 현재 실행 중인 커널에 대해 acpi_call 모듈의 버전 1.2.1 설치:

`dkms install -m {{acpi_call}} -v {{1.2.1}}`

- 모든 커널에서 acpi_call 모듈의 버전 1.2.1 제거:

`dkms remove -m {{acpi_call}} -v {{1.2.1}} --all`
