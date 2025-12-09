# virt-sparsify

> 가상 머신 드라이브 이미지를 Thin Provisioning으로 변환.
> 주의: 데이터 손상을 방지하기 위해 오프라인 상태의 머신에서만 사용하세요.
> 더 많은 정보: <https://manned.org/virt-sparsify>.

- 스냅샷이 없는 상태로 비압축된 이미지를 압축된 스파스 이미지로 생성:

`virt-sparsify --compress {{경로/대상/image.qcow2}} {{경로/대상/image_new.qcow2}}`

- 이미지를 제자리에서 스파스 처리:

`virt-sparsify --in-place {{경로/대상/image.img}}`
