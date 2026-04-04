# ipmitool

> Intelligent Platform Management Interface (IPMI)와 상호작용하기 위한 도구.
> 더 많은 정보: <https://man.freebsd.org/cgi/man.cgi?ipmitool>.

- 로컬 연결을 위해 IPMI 커널 모듈 로드:

`kldload ipmi.ko`

- 로컬 하드웨어에서 IPMI 쉘 실행:

`ipmitool shell`

- 원격 호스트에서 IPMI 쉘 실행:

`ipmitool -H {{ip_주소}} -U {{사용자_이름}} shell`
