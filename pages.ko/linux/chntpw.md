# chntpw

> Windows 레지스트리를 편집하고, 사용자 암호를 재설정하며, 사용자를 관리자로 승격할 수 있는 도구입니다. Windows SAM을 수정하여 동작합니다.
> Kali Linux와 같은 라이브 CD로 대상 머신을 부팅하고, 권한 상승 후 실행하십시오.
> 더 많은 정보: <https://pogostick.net/~pnh/ntpasswd/MANUAL.txt>.

- SAM 파일에 있는 모든 사용자 나열:

`chntpw -l {{경로/대상/sam_파일}}`

- 사용자와 대화형으로 편집:

`chntpw -u {{사용자명}} {{경로/대상/sam_파일}}`

- chntpw를 대화형으로 사용:

`chntpw -i {{경로/대상/sam_파일}}`
