# flatpak run

> Flatpak 애플리케이션 및 런타임 실행.
> 더 많은 정보: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-run>.

- 설치된 애플리케이션 실행:

`flatpak run {{com.example.app}}`

- 특정 브랜치(예: stable, beta, master)에서 설치된 애플리케이션 실행:

`flatpak run --branch={{stable|beta|master|...}} {{com.example.app}}`

- Flatpak 안에서 인터랙티브 셸 실행:

`flatpak run --command={{sh}} {{com.example.app}}`
