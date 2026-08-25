# gdm

> GNOME Display Manager (GDM)는 X Display Manager (XDM)를 대체하는 디스플레이 매니저.
> 관련 항목: `gdm-binary`, `gdmsetup`, `gdm-stop`, `gdm-restart`, `gdm-safe-restart`.
> 더 많은 정보: <https://manned.org/gdm>.

- GNOME Display Manager 애플리케이션 실행:

`gdm`

- `gdm`이 백그라운드 데몬 프로세스로 실행되지 않도록 설정:

`gdm --nodaemon`

- 헤드리스 또는 원격 환경에서 로컬 콘솔 X 서버 `gdm` 관리 비활성화 :

`gdm --no-console`

- `$LD_`로 시작하는 환경 변수 정리 방지:

`gdm --preserve-ld-vars`

- 도움말 표시:

`gdm --help`

- 버전 표시:

`gdm --version`
