# ddrescue

> 손상된 블록 장치에서 데이터를 읽는 데이터 복구 도구.
> 더 많은 정보: <https://www.gnu.org/software/ddrescue/manual/ddrescue_manual.html#Invoking-ddrescue>.

- 장치의 이미지를 생성하고 로그 파일 생성:

`sudo ddrescue {{/dev/sdb}} {{경로/대상/이미지.dd}} {{경로/대상/로그.txt}}`

- 디스크 A를 디스크 B로 클론하고 로그 파일 생성:

`sudo ddrescue {{[-f|--force]}} {{[-n|--no-scrape]}} {{/dev/sdX}} {{/dev/sdY}} {{경로/대상/로그.txt}}`
