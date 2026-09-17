# resticprofile unschedule

> The command removes jobs for schedules declared in the selected profile or group (or of all profiles and groups).
> 관련 항목: `restic`, `resticprofile`, `resticprofile-schedule`.
> 더 많은 정보: <https://creativeprojects.github.io/resticprofile/schedules/configuration/index.html>.

- 지정한 프로필의 백업 스케줄 제거:

`resticprofile unschedule {{[-n|--name]}} "{{프로필_이름}}"`

- 모든 백업 스케줄 제거:

`resticprofile unschedule --all`
