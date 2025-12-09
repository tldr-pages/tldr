# genfstab

> Arch Linux 설치 스크립트로, fstab 파일에 추가할 수 있는 출력 생성.
> 더 많은 정보: <https://manned.org/genfstab>.

- 볼륨 레이블을 기반으로 fstab 호환 출력을 표시:

`genfstab -L {{경로/대상/마운트_포인트}}`

- 볼륨 UUID를 기반으로 fstab 호환 출력을 표시:

`genfstab -U {{경로/대상/마운트_포인트}}`

- 일반적으로 fstab 파일을 생성하는 방법, 루트 권한 필요:

`genfstab -U {{/mnt}} >> {{/mnt/etc/fstab}}`

- 볼륨을 fstab 파일에 추가하여 자동으로 마운트:

`genfstab -U {{경로/대상/마운트_포인트}} | sudo tee -a /etc/fstab`
