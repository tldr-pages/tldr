# flatpak-builder

> 애플리케이션의 의존성 빌드를 지원합니다.
> 더 많은 정보: <https://docs.flatpak.org/en/latest/flatpak-builder-command-reference.html>.

- Flatpak을 빌드하고 새 저장소에 내보내기:

`flatpak-builder {{경로/대상/빌드_디렉토리}} {{경로/대상/매니페스트}}`

- Flatpak을 빌드하고 지정된 저장소에 내보내기:

`flatpak-builder --repo={{저장소_이름}} {{경로/대상/빌드_디렉토리}} {{경로/대상/매니페스트}}`

- Flatpak을 빌드하고 로컬에 설치:

`flatpak-builder --install {{경로/대상/빌드_디렉토리}} {{경로/대상/매니페스트}}`

- Flatpak을 빌드하고 서명하여 지정된 저장소에 내보내기:

`flatpak-builder --gpg-sign={{키_아이디}} --repo={{저장소_이름}} {{경로/대상/매니페스트}}`

- 애플리케이션 샌드박스 내부에서 설치 없이 셸 실행:

`flatpak-builder --run {{경로/대상/빌드_디렉토리}} {{경로/대상/매니페스트}} {{sh}}`
