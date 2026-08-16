# resticprofile schedule

> 백업 작업을 예약 및 백그라운드 실행.
> 관련 항목: `restic`, `resticprofile`, `resticprofile-unschedule`.
> 더 많은 정보: <https://creativeprojects.github.io/resticprofile/schedules/configuration/index.html>.

- 기본 프로필의 백업 스케줄 설정:

`resticprofile schedule`

- 지정한 프로필의 백업 스케줄 설정 (기본 프로필 이름은 "default"):

`resticprofile --name "{{그룹_이름}}" schedule`

- 모든 프로필의 백업 스케줄 설정:

`resticprofile schedule --all`

- 스케줄 작업을 설치한 후 바로 시작하지 않음:

`resticprofile schedule --no-start`

- 지정한 프로필의 예약된 작업 상태 표시:

`resticprofile status {{[-n|--name]}} {{프로필_이름}}`

- 예약된 작업을 수동으로 실행 (시스템 스케줄러에서 사용):

`resticprofile run-schedule "backup@{{프로필_이름}}"`
