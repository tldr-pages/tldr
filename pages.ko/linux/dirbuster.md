# dirbuster

> 서버에서 디렉터리와 파일명을 무차별 대입으로 찾기.
> 더 많은 정보: <https://www.kali.org/tools/dirbuster/>.

- GUI 모드로 시작:

`dirbuster -u {{http://example.com}}`

- 헤드리스(무 GUI) 모드로 시작:

`dirbuster -H -u {{http://example.com}}`

- 파일 확장자 목록 설정:

`dirbuster -e {{txt,html}}`

- 자세한 출력 활성화:

`dirbuster -v`

- 보고서 위치 설정:

`dirbuster -r {{경로/대상/보고서.txt}}`
