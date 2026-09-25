# resticprofile unschedule

> 선택한 프로필 또는 그룹에 정의된 스케줄 작업을 제거. (모든 프로필 및 그룹의 스케줄 작업 제거도 가능).
> 관련 항목: `restic`, `resticprofile schedule`.
> 더 많은 정보: <https://creativeprojects.github.io/resticprofile/schedules/configuration/index.html>.

- 지정한 프로필의 백업 스케줄 제거:

`resticprofile unschedule {{[-n|--name]}} "{{프로필_이름}}"`

- 모든 백업 스케줄 제거:

`resticprofile unschedule --all`
