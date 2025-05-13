# unshadow

> 시스템이 섀도우 비밀번호를 사용하는 경우 전통적인 유닉스 비밀번호 파일을 얻기 위해 John the Ripper 프로젝트에서 제공하는 유틸리티.
> 더 많은 정보: <https://www.openwall.com/john/doc/>.

- 현재 시스템의 `/etc/shadow`와 `/etc/passwd` 결합:

`sudo unshadow /etc/passwd /etc/shadow`

- 임의의 섀도우 및 비밀번호 [f]파일 결합:

`sudo unshadow {{경로/대상/passwd}} {{경로/대상/shadow}}`
