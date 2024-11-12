# mist

> MIST - macOS Installer Super Tool.
> macOS 펌웨어/설치 프로그램을 자동으로 다운로드합니다.
> 더 많은 정보: <https://github.com/ninxsoft/mist-cli>.

- Apple Silicon Mac용 모든 사용 가능한 macOS 펌웨어 나열:

`mist list firmware`

- Intel Mac용 모든 사용 가능한 macOS 설치 프로그램 나열, macOS Big Sur 및 이후 버전의 범용 설치 프로그램 포함:

`mist list installer`

- 이 Mac과 호환되는 모든 macOS 설치 프로그램 나열, macOS Big Sur 및 이후 버전의 범용 설치 프로그램 포함:

`mist list installer --compatible`

- Intel Mac용 모든 사용 가능한 macOS 설치 프로그램 나열, 베타 버전 포함, macOS Big Sur 및 이후 버전의 범용 설치 프로그램 포함:

`mist list installer --include-betas`

- Intel Mac용 최신 macOS Sonoma 설치 프로그램만 나열, macOS Big Sur 및 이후 버전의 범용 설치 프로그램 포함:

`mist list installer --latest "macOS Sonoma"`

- macOS 설치 프로그램을 CSV [f]파일로 내보내기:

`mist list installer --export "{{경로/대상/export.csv}}"`

- Apple Silicon Mac용 최신 macOS Sonoma 펌웨어 다운로드, 사용자 지정 이름 사용:

`mist download firmware "macOS Sonoma" --firmware-name "{{Install %NAME% %VERSION%-%BUILD%.ipsw}}"`

- Intel Mac용 특정 macOS 설치 프로그램 버전 다운로드, macOS Big Sur 및 이후 버전의 범용 설치 프로그램 포함:

`mist download installer "{{13.5.2}}" application`
