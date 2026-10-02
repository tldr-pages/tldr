# flatpak update

> flatpak 애플리케이션과 런타임을 업데이트.
> 더 많은 정보: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-update>.

- 설치된 모든 애플리케이션과 런타임 업데이트 (`-y` 옵션을 사용하면 모든 확인 메시지에 자동으로 동의):

`flatpak update`

- 지정한 애플리케이션만 업데이트:

`flatpak update {{com.example.app}}`

- 지정한 커밋 버전으로 업데이트 또는 다운그레이드 (flatpak remote-info, flatpak mask 참고):

`flatpak update --commit {{COMMIT}} {{com.example.app}}`
