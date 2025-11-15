# virt-clone

> libvirt 가상 머신 복제.
> 더 많은 정보: <https://manned.org/virt-clone>.

- 가상 머신을 복제하고 새 이름, 저장 경로 및 MAC 주소를 자동으로 생성:

`virt-clone --original {{가상머신_이름}} --auto-clone`

- 가상 머신을 복제하고 새 이름, 저장 경로 및 MAC 주소를 지정:

`virt-clone --original {{가상머신_이름}} --name {{새_가상머신_이름}} --file {{경로/대상/새_저장소}} --mac {{ff:ff:ff:ff:ff:ff|RANDOM}}`
