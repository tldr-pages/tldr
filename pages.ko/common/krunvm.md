# krunvm

> OCI 이미지를 사용하여 MicroVM을 생성.
> 더 많은 정보: <https://github.com/containers/krunvm>.

- Fedora 기반 MicroVM 생성:

`krunvm create {{docker.io/fedora}} --cpus {{vCPU_수}} --mem {{메모리_메가바이트}} --name "{{이름}}"`

- 특정 이미지 시작:

`krunvm start "{{이미지_이름}}"`

- 이미지 나열:

`krunvm list`

- 특정 이미지 변경:

`krunvm changevm --cpus {{vCPU_수}} --mem {{메모리_메가바이트}} --name "{{새_VM_이름}}" "{{현재_VM_이름}}"`

- 특정 이미지 삭제:

`krunvm delete "{{이미지_이름}}"`
