# VBoxManage cloud

> 클라우드 인스턴스 및 이미지를 관리하기 위한 VirtualBox 명령줄 인터페이스.
> 더 많은 정보: <https://www.virtualbox.org/manual/ch08.html#vboxmanage-cloud>.

- 지정된 구획에 속하는 특정 상태의 인스턴스 나열:

`VBoxManage cloud --provider={{제공자_이름}} --profile={{프로필_이름}} list instances --state={{running|terminated|paused}} --compartment-id={{구획_id}}`

- 새 인스턴스 생성:

`VBoxManage cloud --provider={{제공자_이름}} --profile={{프로필_이름}} instance create --domain-name={{도메인_이름}} --image-id={{이미지_id}} | {{--옵션...}}`

- 특정 인스턴스에 대한 정보 수집:

`VBoxManage cloud --provider={{제공자_이름}} --profile={{프로필_이름}} instance info --id={{고유_id}}`

- 인스턴스 종료:

`VBoxManage cloud --provider={{제공자_이름}} --profile={{프로필_이름}} instance terminate --id={{고유_id}}`

- 특정 구획 및 상태의 이미지 나열:

`VBoxManage cloud --provider={{제공자_이름}} --profile={{프로필_이름}} list images --compartment-id={{구획_id}} --state={{상태_이름}}`

- 새 이미지 생성:

`VBoxManage cloud --provider={{제공자_이름}} --profile={{프로필_이름}} image create --instance-id={{인스턴스_id}} --display-name={{표시_이름}} --compartment-id={{구획_id}}`

- 특정 이미지에 대한 정보 검색:

`VBoxManage cloud --provider={{제공자_이름}} --profile={{프로필_이름}} image info --id={{고유_id}}`

- 이미지 삭제:

`VBoxManage cloud --provider={{제공자_이름}} --profile={{프로필_이름}} image delete --id={{고유_id}}`
