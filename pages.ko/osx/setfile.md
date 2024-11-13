# setfile

> HFS+ 디렉터리 내 파일의 속성을 설정합니다.
> 더 많은 정보: <https://ss64.com/osx/setfile.html>.

- 특정 파일의 생성 날짜 설정:

`setfile -d "{{MM/DD/YYYY HH:MM:SS}}" {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 특정 파일의 수정 날짜 설정:

`setfile -m "{{MM/DD/YYYY HH:MM:SS}}" {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 심볼릭 링크 파일의 수정 날짜 설정 (링크된 파일 자체는 아님):

`setfile -P -m "{{MM/DD/YYYY HH:MM:SS}}" {{경로/대상/파일1 경로/대상/파일2 ...}}`
