# pip lock

> Python 패키지와 의존성을 재현 가능한 파일로 고정.
> `pip`의 실험적 기능.
> 더 많은 정보: <https://pip.pypa.io/en/stable/cli/pip_lock/>.

- 현재 프로젝트용 `pylock.toml` 생성:

`pip lock {{[-e|--editable]}} .`

- requirements 파일의 의존성을 lock 파일로 생성:

`pip lock {{[-r|--requirement]}} {{경로/대상/requirements.txt}}`

- 사용자 지정 출력 파일로 lock 저장:

`pip lock {{[-o|--output]}} {{경로/대상/lockfile.toml}}`

- 특정 패키지와 해당 의존성 lock 생성:

`pip lock {{패키지}}`
