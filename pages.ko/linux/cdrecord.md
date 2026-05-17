# cdrecord

> CD 또는 DVD에 데이터를 기록하는 도구.
> 일부 cdrecord 명령은 디스크 데이터 전체 삭제같은 파괴적인 작업 수행 가능.
> 더 많은 정보: <https://manned.org/cdrecord>.

- `cdrecord`에서 사용할 수 있는 광학 드라이브 목록 표시:

`cdrecord --devices`

- 오디오 전용 디스크 기록(Record) 또는 굽기(burn):

`cdrecord dev={{/dev/optical_drive}} -audio {{track*.cdaudio}}`

- 파일을 디스크에 굽고, 완료 후 디스크 꺼내기 (일부 레코더는 필요):

`cdrecord -eject dev={{/dev/optical_drive}} -data {{파일.iso}}`

- 광학 드라이브 디스크에 파일 굽기(여러 디스크에 연속으로 기록 가능):

`cdrecord -tao dev={{/dev/optical_drive}} -data {{파일.iso}}`
