# podman login

> 컨테이너 레지스트리에 로그인.
> 참고: Linux의 기본 인증 파일 경로는 `$XDG_RUNTIME_DIR/containers/auth.json`이며, 일반적으로 RAM 기반의 `tmpfs`에 저장됨.
> 더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-login.1.html>.

- 레지스트리에 로그인 (Linux에서는 비영구적; Windows/macOS에서는 영구적):

`podman login {{registry.example.org}}`

- Linux에서 인증 정보를 영구저긍로 저장하며 레지스트리에 로그인:

`podman login --authfile $HOME/.config/containers/auth.json {{registry.example.org}}`

- 안전하지 않은 (HTTP) 레지스트리에 로그인:

`podman login --tls-verify false {{registry.example.org}}`
