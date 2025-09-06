# gitlab

> GitLab API용 Ruby 래퍼.
> `ctl`과 같은 일부 하위 명령에는 자체 사용법 문서가 존재.
> 더 많은 정보: <https://narkoz.github.io/gitlab/>.

- 새로운 프로젝트를 생성:

`gitlab create_project {{프로젝트_이름}}`

- 특정 커밋에 대한 정보를 얻기:

`gitlab commit {{프로젝트_이름}} {{커밋_해시}}`

- CI 파이프라인의 작업에 대한 정보를 얻기:

`gitlab pipeline_jobs {{프로젝트_이름}} {{파이프라인_아이디}}`

- 특정 CI 작업을 시작:

`gitlab job_play {{프로젝트_이름}} {{작업_아이디}}`
