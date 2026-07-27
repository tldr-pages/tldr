# flatpak remote-info

> 원격 저장소에 있는 애플리케이션 또는 런타임 정보를 표시.
> 더 많은 정보: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remote-info>.

- flatpak 애플리케이션 정보 표시:

`flatpak remote-info {{원격저장소_이름}} {{com.example.app}}`

- 원격 저장소의 이전 버전 변경 이력 표시:

`flatpak remote-info --log {{원격저장소_이름}} {{com.example.app}}`

- 최신 버전 대신, 지정한 커밋의 정보 표시:

`flatpak remote-info --commit {{COMMIT}} {{원격저장소_이름}} {{com.example.app}}`
