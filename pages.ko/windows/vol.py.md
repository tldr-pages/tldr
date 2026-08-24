# vol.py

> 휘발성 메모리(RAM) 덤프를 분석하는 포렌식 프레임워크.
> volatility3에서는 플러그인이 운영체제 기반으로 구성됨. 아럐 예는 Windows 기준.
> 더 많은 정보: <https://volatility3.readthedocs.io/en/latest/index.html>.

- 메모리 덤프 파일 정보 확인:

`python3 vol.py {{[-f|--filename]}} {{경로\대상\메모리_덤프_파일}} windows.info`

- 활성화 프로세스 목록 나열:

`python3 vol.py {{[-f|--filename]}} {{경로\대상\메모리_덤프_파일}} windows.pslist`

- 시스템 사용자 해시 목록 확인:

`python3 vol.py {{[-f|--filename]}} {{경로\대상\메모리_덤프_파일}} windows.hashdump`

- 활성 네트워크 연결 목록 확인:

`python3 vol.py {{[-f|--filename]}} {{경로\대상\메모리_덤프_파일}} windows.netstat`

- 도움말 표시:

`python3 vol.py {{[-h|--help]}}`
