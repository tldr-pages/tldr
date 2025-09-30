# pvcreate

> 디스크 또는 파티션을 물리적 볼륨으로 초기화합니다.
> 같이 보기: `lvm`.
> 더 많은 정보: <https://manned.org/pvcreate>.

- LVM에서 사용할 수 있도록 `/dev/sda1` 볼륨 초기화:

`pvcreate {{/dev/sda1}}`

- 확인 프롬프트 없이 강제로 생성:

`pvcreate --force {{/dev/sda1}}`
