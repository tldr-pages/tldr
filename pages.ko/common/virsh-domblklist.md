# virsh-domblklist

> 가상 머신과 연결된 블록 장치에 대한 정보 나열.
> 같이 보기: `virsh`.
> 더 많은 정보: <https://manned.org/virsh>.

- 블록 장치의 대상 이름 및 소스 경로 나열:

`virsh domblklist --domain {{가상머신_이름}}`

- 디스크 유형, 장치 값, 대상 이름 및 소스 경로 나열:

`virsh domblklist --domain {{가상머신_이름}} --details`
