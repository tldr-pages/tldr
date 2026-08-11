# reg.py

> SMB/RPC를 통해 원격 Windows 시스템의 레지스트리 키와 값을 조회, 추가, 삭제, 저장 또는 백업.
> Impacket 도구의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 지정한 레지스트리 경로의 하위 키와 값 조회:

`reg.py {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}} query -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}'`

- 지정한 레지스트리 경로의 모든 하위 키와 값을 재귀적으로 조회:

`reg.py {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}} query -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}' -s`

- 새로운 레지스트리 키 또는 값 추가 (기본 값 형식: `REG_SZ`):

`reg.py {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}} add -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}' -v {{값_이름}} -vt {{REG_SZ|REG_NONE|REG_EXPAND_SZ|REG_BINARY|REG_DWORD|REG_DWORD_BIG_ENDIAN|REG_LINK|REG_MULTI_SZ|REG_QWORD}} -vd {{값_데이터}}`

- 레지스트리 키 또는 값 삭제:

`reg.py {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}} delete -keyName '{{HKLM\SOFTWARE\Example}}' -v {{값_이름}}`

- 레지스트리 키 및 하위 키를 UNC 경로를 통해 대상 시스템 파일로 저장:

`reg.py {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}} save -keyName '{{HKLM\SOFTWARE\Example}}' -o '\\{{대상}}\{{공유}}\{{출력_파일.reg}}'`

- SAM, SYSTEM, SECURITY 하이브를 UNC 경로를 통해 대상 시스템에 백업 (SYSTEM 권한 필요):

`reg.py {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}} backup -o '\\{{대상}}\{{공유}}'`
