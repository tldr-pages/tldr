# virt-viewer

> 가상 머신(VM)을 위한 최소한의 그래픽 인터페이스.
> 참고: '도메인'은 기존 VM의 이름, UUID 또는 ID를 의미합니다 (참조: tldr virsh).
> 더 많은 정보: <https://manned.org/virt-viewer>.

- 실행 중인 가상 머신을 선택할 수 있는 프롬프트로 `virt-viewer` 시작:

`virt-viewer`

- ID, UUID 또는 이름으로 특정 가상 머신에 대해 `virt-viewer` 시작:

`virt-viewer "{{도메인}}"`

- 가상 머신이 시작될 때까지 기다리고 종료 후 재시작되면 자동으로 다시 연결:

`virt-viewer --reconnect --wait "{{도메인}}"`

- TLS를 통해 특정 원격 가상 머신에 연결:

`virt-viewer --connect "xen//{{URL}}" "{{도메인}}"`

- SSH를 통해 특정 원격 가상 머신에 연결:

`virt-viewer --connect "qemu+ssh//{{사용자명}}@{{URL}}/system" "{{도메인}}"`
