# diffstat

> `diff` 명령어의 결과로부터 히스토그램을 생성한다.
> 더 많은 정보: <https://manned.org/diffstat>.

- 히스토그램에서 변경점들 표시:

`diff {{경로/대상/파일1}} {{경로/대상/파일2}} | diffstat`

- 삽입, 삭제 및 수정된 변경점들을 테이블로 표시:

`diff {{경로/대상/파일1}} {{경로/대상/파일2}} | diffstat -t`
