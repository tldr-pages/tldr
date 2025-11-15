# ospp.vbs

> Microsoft Office 제품의 볼륨 라이선스 버전을 설치, 활성화 및 관리합니다.
> 참고: 이 명령어는 현재 볼륨 라이선스가 있는 Office 제품 버전을 덮어쓰거나 비활성화하거나 제거할 수 있으므로 주의하여 진행하세요.
> 더 많은 정보: <https://learn.microsoft.com/deployoffice/vlactivation/tools-to-manage-volume-activation-of-office>.

- 제품 키 설치 (참고: 기존 키를 덮어씀):

`cscript ospp.vbs /inpkey:{{제품_키}}`

- 설치된 제품 키 제거 (제품 키의 마지막 다섯 자리 숫자 사용):

`cscript ospp.vbs /unpkey:{{제품_키_숫자}}`

- KMS 호스트 이름 설정:

`cscript ospp.vbs /sethst:{{아이피|호스트명}}`

- KMS 포트 설정:

`cscript ospp.vbs /setprt:{{포트}}`

- 설치된 Office 제품 키 활성화:

`cscript ospp.vbs /act`

- 설치된 제품 키에 대한 라이선스 정보 표시:

`cscript ospp.vbs /dstatus`
