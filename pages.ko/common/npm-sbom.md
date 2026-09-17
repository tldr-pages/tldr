# npm sbom

> Node.js 프로젝트의 Software Bill of Materials (SBOM)을 생성하는 명령어.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-sbom/>.

- 프로젝트의 모든 의존성 목록 출력:

`npm sbom`

- `dev` 및 `optional` 의존성 제외:

`npm sbom --omit dev --omit optional`

- 오직 `package-lock.json`을 기반으로 SBOM 생성:

`npm sbom --package-lock-only`
