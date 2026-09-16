# ipmitool

> Intelligent Platform Management Interface (IPMI)와 상호작용하는 도구.
> 더 많은 정보: <https://manned.org/ipmitool>.

- 로컬 연결을 위한 IPMI 드라이버 시작:

`systemctl start ipmidrv`

- 로컬 시스템에서 IPMI 쉘 실행:

`sudo ipmitool shell`

- 원격 호스트에서 IPMI 쉘 실행:

`ipmitool -H {{ip_주소}} -U {{사용자_이름}} shell`
