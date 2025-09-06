# systemd-creds

> 서비스 자격 증명을 나열, 표시, 암호화 및 복호화.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-creds.html>.

- 파일을 암호화하고 특정 이름 설정:

`systemd-creds encrypt --name={{이름}} {{경로/대상/입력_파일}} {{경로/대상/출력}}`

- 파일을 다시 복호화:

`systemd-creds decrypt {{경로/대상/입력_파일}} {{경로/대상/출력_파일}}`

- `stdin`에서 텍스트 암호화:

`echo -n {{텍스트}} | systemd-creds encrypt --name={{이름}} - {{경로/대상/출력}}`

- 텍스트를 암호화하고 서비스 파일에 추가 (자격 증명은 `$CREDENTIALS_DIRECTORY`에서 사용 가능):

`echo -n {{텍스트}} | systemd-creds encrypt --name={{이름}} --pretty - - >> {{서비스}}`

- 주어진 타임스탬프까지 유효한 자격 증명 생성:

`systemd-creds encrypt --not-after="{{타임스탬프}}" {{경로/대상/입력_파일}} {{경로/대상/출력_파일}}`
