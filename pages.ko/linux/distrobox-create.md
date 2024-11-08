# distrobox-create

> Distrobox 컨테이너 생성. 같이 보기: `tldr distrobox`.
> 생성된 컨테이너는 호스트와 밀접하게 통합되어 사용자의 HOME 디렉토리, 외부 저장소, 외부 USB 장치, 그래픽 애플리케이션(X11/Wayland), 오디오를 공유할 수 있습니다.
> 더 많은 정보: <https://distrobox.it/usage/distrobox-create>.

- Ubuntu 이미지로 Distrobox 컨테이너 생성:

`distrobox-create {{컨테이너_이름}} --image {{ubuntu:latest}}`

- Distrobox 컨테이너 복제:

`distrobox-create --clone {{컨테이너_이름}} {{복제된_컨테이너_이름}}`
