# pamexec

> Netpbm 파일의 각 이미지에 대해 셸 명령을 실행.
> 같이 보기: `pamfile`, `pampick`, `pamsplit`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamexec.html>.

- Netpbm 파일의 각 이미지에 대해 셸 명령 실행:

`pamexec {{명령}} {{경로/대상/이미지.pam}}`

- 명령이 비정상 종료 상태로 종료되면 처리를 중단:

`pamexec {{명령}} {{경로/대상/이미지.pam}} {{[-c|-check]}}`
