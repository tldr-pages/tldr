# virsh-connect

> 가상 머신 하이퍼바이저에 연결합니다.
> 같이 보기: `virsh`.
> 더 많은 정보: <https://manned.org/virsh>.

- 기본 하이퍼바이저에 연결:

`virsh connect`

- 로컬 QEMU/KVM 하이퍼바이저에 루트로 연결:

`virsh connect qemu:///system`

- 하이퍼바이저의 새 인스턴스를 시작하고, 로컬 사용자로 연결:

`virsh connect qemu:///session`

- SSH를 사용하여 원격 하이퍼바이저에 루트로 연결:

`virsh connect qemu+ssh://{{사용자_명@호스트_명}}/system`
