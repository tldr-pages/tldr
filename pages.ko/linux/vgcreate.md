# vgcreate

> 여러 대용량 저장 장치를 결합하여 볼륨 그룹 생성.
> 같이 보기: `lvm`.
> 더 많은 정보: <https://manned.org/vgcreate>.

- `/dev/sda1` 장치를 사용하여 vg1이라는 새 볼륨 그룹 생성:

`vgcreate {{vg1}} {{/dev/sda1}}`

- 여러 장치를 사용하여 vg1이라는 새 볼륨 그룹 생성:

`vgcreate {{vg1}} {{/dev/sda1}} {{/dev/sdb1}} {{/dev/sdc1}}`
