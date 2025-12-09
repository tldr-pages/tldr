# virt-sysprep

> 가상 머신 이미지를 재설정, 비구성 또는 사용자 정의.
> 더 많은 정보: <https://manned.org/virt-sysprep>.

- 지원되는 모든 작업 나열 (활성화된 작업은 별표로 표시됨):

`virt-sysprep --list-operations`

- 활성화된 모든 작업을 실행하되 실제로 변경사항을 적용하지 않음:

`virt-sysprep --domain {{가상_머신_이름}} --dry-run`

- 지정된 작업만 실행:

`virt-sysprep --domain {{가상_머신_이름}} --operations {{작업1,작업2,...}}`

- 새로운 `/etc/machine-id` 파일을 생성하고 사용자 정의를 활성화하여 네트워크 충돌을 피하기 위해 호스트 이름을 변경할 수 있도록 설정:

`virt-sysprep --domain {{가상_머신_이름}} --enable {{사용자_정의}} --hostname {{호스트_이름}} --operation {{machine-id}}`
