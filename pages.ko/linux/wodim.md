# wodim

> CD 또는 DVD에 데이터를 기록하는 명령어(일부 시스템에서는 `cdrecord`로 별칭됨).
> wodim의 일부 사용은 디스크의 모든 데이터를 지우는 등의 파괴적 작업을 수행할 수 있습니다.
> 더 많은 정보: <https://manned.org/wodim>.

- `wodim`에서 사용할 수 있는 광학 드라이브 표시:

`wodim --devices`

- 오디오 전용 디스크 기록(굽기):

`wodim dev={{/dev/optical_drive}} -audio {{track*.cdaudio}}`

- 파일을 디스크에 굽고 완료 시 디스크 배출(일부 레코더는 이 작업이 필요함):

`wodim -eject dev={{/dev/optical_drive}} -data {{파일.iso}}`

- 광학 드라이브에 파일을 굽고, 연속적으로 여러 디스크에 기록할 수 있음:

`wodim -tao dev={{/dev/optical_drive}} -data {{파일.iso}}`
