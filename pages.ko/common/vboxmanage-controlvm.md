# VBoxManage controlvm

> 현재 실행 중인 가상 머신의 상태 및 설정 변경.
> 더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-controlvm>.

- 가상 머신의 실행을 일시 중지:

`VBoxManage controlvm {{uuid|vm_이름}} pause`

- 일시 중지된 가상 머신의 실행 재개:

`VBoxManage controlvm {{uuid|vm_이름}} resume`

- 가상 머신에 콜드 리셋 수행:

`VBoxManage controlvm {{uuid|vm_이름}} reset`

- 가상 머신의 전원을 컴퓨터의 전원 케이블을 뽑는 것과 동일한 효과로 끄기:

`VBoxManage controlvm {{uuid|vm_이름}} poweroff`

- 가상 머신을 종료하고 현재 상태 저장:

`VBoxManage controlvm {{uuid|vm_이름}} savestate`

- 가상 머신에 ACPI(Advanced Configuration and Power Interface) 종료 신호 보내기:

`VBoxManage controlvm {{uuid|vm_이름}} acpipowerbutton`

- 게스트 OS에 가상 머신의 자체 재부팅 명령 보내기:

`VBoxManage controlvm {{uuid|vm_이름}} reboot`

- 상태를 저장하지 않고 가상 머신 종료:

`VBoxManage controlvm {{uuid|vm_이름}} shutdown`
