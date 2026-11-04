# ipmitool

> IPMI(Intelligent Platform Management Interface)와 상호작용하는 도구.
> 더 많은 정보: <https://manned.org/ipmitool>.

- 로컬 하드웨어에서 IPMI 쉘 실행:

`sudo ipmitool shell`

- 원격 호스트에서 IPMI 쉘 실행:

`ipmitool -H {{ip_주소}} -U {{사용자명}} shell`
