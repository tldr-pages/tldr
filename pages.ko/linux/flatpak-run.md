# flatpak run

> flatpak 애플리케이션 및 런타임 실행.
> 더 많은 정보: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-run>.

- 설치된 애플리케이션 실행:

`flatpak run {{com.example.app}}`

- 지정한 브랜치(예: stable, beta, master)의 애플리케이션 실행:

`flatpak run --branch={{stable|beta|master|...}} {{com.example.app}}`

- flatpak 환경에서 대화형 셸 실행:

`flatpak run --command={{sh}} {{com.example.app}}`

- 지정한 런타임 버전으로 애플리케이션 실행:

`flatpak run --runtime-version={{24.08|master|stable|...}} {{com.example.app}}`

- 다른 런타임(동일한 버전 번호)을 사용하여 애플리케이션 실행:

`flatpak run --runtime={{org.freedesktop.Sdk}} {{com.example.app}}`
