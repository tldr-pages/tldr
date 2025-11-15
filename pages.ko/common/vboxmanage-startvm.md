# VBoxManage startvm

> 가상 머신 시작.
> 더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-startvm>.

- 가상 머신 시작:

`VBoxManage startvm {{vm_이름|uuid}}`

- 지정된 UI 모드로 가상 머신 시작:

`VBoxManage startvm {{vm_이름|uuid}} --type {{headless|gui|sdl|separate}}`

- 암호화된 가상 머신을 시작하기 위해 암호 파일 지정:

`VBoxManage startvm {{vm_이름|uuid}} --password {{경로/대상/암호_파일}}`

- 암호화된 가상 머신을 시작하기 위해 암호 ID 지정:

`VBoxManage startvm {{vm_이름|uuid}} --password-id {{암호_id}}`

- 환경 변수 쌍 이름 값을 사용하여 가상 머신 시작:

`VBoxManage startvm {{vm_이름|uuid}} --put-env={{이름}}={{값}}`
