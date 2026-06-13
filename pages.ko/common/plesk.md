# plesk

> Plesk 호스팅 제어 패널.
> 더 많은 정보: <https://docs.plesk.com/en-US/obsidian/cli-linux/plesk-utility.75661/>.

- 관리자 사용자에 대한 자동 로그인 링크 생성 및 출력:

`plesk login`

- 제품 버전 정보 표시:

`plesk version`

- 호스팅된 모든 도메인 나열:

`plesk bin domain --list`

- `panel.log` 파일에서 변경 사항 감시 시작:

`plesk log {{panel.log}}`

- 대화형 MySQL 콘솔 시작:

`plesk db`

- 기본 편집기로 Plesk 메인 구성 파일 열기:

`plesk conf {{panel.ini}}`
