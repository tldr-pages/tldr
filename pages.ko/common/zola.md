# zola

> 단일 실행 파일에 모든 기능이 들어있는 정적 사이트 생성기.
> 더 많은 정보: <https://www.getzola.org/documentation/getting-started/cli-usage/>.

- 주어진 디렉토리에 Zola가 사용하는 디렉토리 구조를 생성:

`zola init {{내_사이트_이름}}`

- `public` 디렉토리에 전체 사이트를 빌드 (이미 존재하는 디렉토리가 있다면 삭제):

`zola build`

- 별도의 디렉토리에 전체 사이트를 빌드:

`zola build --output-dir {{경로/대상/폴더/}}`

- 사이트를 빌드하고 로컬 서버를 사용하여 제공 (기본 주소는 `127.0.0.1:1111`):

`zola serve`

- `build` 명령어와 같이 모든 페이지를 빌드하지만, 그 결과를 디스크에 기록하지는 않음:

`zola check`
