# vgchange

> 논리 볼륨 관리자(LVM) 볼륨 그룹의 속성을 변경합니다.
> 같이 보기: `lvm`.
> 더 많은 정보: <https://manned.org/vgchange>.

- 모든 볼륨 그룹의 논리 볼륨 활성화 상태 변경:

`sudo vgchange --activate {{y|n}}`

- 지정된 볼륨 그룹의 논리 볼륨 활성화 상태 변경 (`vgscan`으로 확인 가능):

`sudo vgchange --activate {{y|n}} {{볼륨_그룹}}`
