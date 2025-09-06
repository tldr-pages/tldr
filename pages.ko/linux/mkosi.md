# mkosi

> 모던하고 레거시가 없는 리눅스 이미지를 빌드합니다.
> `systemd`의 일부입니다.
> 더 많은 정보: <https://manned.org/mkosi>.

- 현재 빌드 구성을 표시하여 빌드될 내용을 확인:

`mkosi summary`

- 기본 설정으로 이미지 빌드 (배포판이 선택되지 않은 경우 호스트 시스템의 배포판 사용):

`mkosi build --distribution {{fedora|debian|ubuntu|arch|opensuse|...}}`

- 이미지를 빌드하고 해당 이미지의 systemd-nspawn 컨테이너에서 대화형 셸 실행:

`mkosi shell`

- QEMU를 사용하여 가상 머신에서 이미지 부팅 (디스크 이미지 또는 커널이 제공된 CPIO 이미지에 대해서만 지원):

`mkosi qemu`

- 도움말 표시:

`mkosi help`
