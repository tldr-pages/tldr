# moro

> 작업 시간을 추적.
> 더 많은 정보: <https://github.com/getmoro/moro/blob/master/DOCUMENTATION.md>.

- 매개변수 없이 `moro`를 호출하여 현재 시간을 작업 시작 시간으로 설정:

`moro`

- 작업 시작 시간을 사용자 정의 시간으로 지정:

`moro hi {{09:30}}`

- 매개변수 없이 `moro`를 두 번째로 호출하여 현재 시간을 작업 종료 시간으로 설정:

`moro`

- 작업 종료 시간을 사용자 정의 시간으로 지정:

`moro bye {{17:30}}`

- 현재 작업일에 메모 추가:

`moro note {{3시간 프로젝트 Foo}}`

- 현재 작업일의 시간 기록 및 메모 보고서 표시:

`moro report`

- 기록된 모든 작업일의 시간 기록 및 메모 보고서 표시:

`moro report --all`
