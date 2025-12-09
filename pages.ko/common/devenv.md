# devenv

> Nix를 사용하여 빠르고, 선언적이며, 재현 가능하고 구성 가능한 개발자 환경을 의미.
> 더 많은 정보: <https://devenv.sh/getting-started/#commands>.

- 환경 초기화:

`devenv init`

- 완화된 기밀성 (밀폐된 상태)로 개발 환경에 진입:

`devenv shell --impure`

- 현재 환경에 대한 자세한 정보를 얻기:

`devenv info --verbose`

- `devenv`로 프로세스를 시작:

`devenv up --config /{{파일}}/{{경로}}/`

- 환경 변수를 정리하고 오프라인 모드에서 쉘을 재입력:

`devenv --clean --offline`

- 이전 쉘 세대를 삭제:

`devenv gc`
