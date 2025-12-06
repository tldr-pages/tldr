# toolbox create

> 새 Toolbx 컨테이너 생성.
> 더 많은 정보: <https://manned.org/toolbox-create.1>.

- 특정 배포판에 대한 Toolbx 컨테이너 생성:

`toolbox create --distro {{배포판}}`

- 현재 배포판의 특정 릴리스에 대한 Toolbx 컨테이너 생성:

`toolbox create --release {{릴리스}}`

- 사용자 지정 이미지로 Toolbx 컨테이너 생성:

`toolbox create --image {{이름}}`

- 사용자 지정 Fedora 이미지에서 Toolbx 컨테이너 생성:

`toolbox create --image {{registry.fedoraproject.org/fedora-toolbox:39}}`

- Fedora 39의 기본 이미지를 사용하여 Toolbx 컨테이너 생성:

`toolbox create --distro {{fedora}} --release {{f39}}`
