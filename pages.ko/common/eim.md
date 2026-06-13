# eim

> ESP-IDF를 설치하고 관리하는 도구.
> 더 많은 정보: <https://docs.espressif.com/projects/idf-im-ui/en/latest/cli_commands.html>.

- 기본 위치에 최신 ESP-IDF 버전 설치 (Windows: `C:\esp`, POSIX: `~/.espressif`):

`eim install`

- 특정 ESP-IDF 버전 설치:

`eim install {{[-i|--idf-versions]}} {{v5.3.2}}`

- 대화형 설치 마법사 실행:

`eim wizard`

- 사용자 지정 경로에 특정 버전을 설치하며, 대화형 모드 강제 활성화 (프롬프트를 통해 설치 가능):

`eim install {{[-i|--idf-versions]}} {{v5.3.2}} {{[-p|--path]}} {{/opt/esp-idf}} {{[-n|--non-interactive]}} false`

- 현재 설치된 모든 ESP-IDF 버전 목록 출력:

`eim list`

- 특정 ESP-IDF 버전 제거:

`eim remove {{v5.3.2}}`

- TOML 설정 파일을 사용하여 headless 모드로 설치:

`eim install {{[-c|--config]}} {{경로/대상/구성파일.toml}}`

- 미리 다운로드된 아카이브 파일을 사용하여 오프라인 설치:

`eim install --use-local-archive {{경로/대상/아카이브.zst}}`
