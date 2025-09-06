# roave-backward-compatibility-check

> PHP 라이브러리의 두 버전 간 호환성 파손 여부를 확인.
> 더 많은 정보: <https://github.com/Roave/BackwardCompatibilityCheck>.

- 마지막 태그 이후의 호환성 파손 점검:

`roave-backward-compatibility-check`

- 특정 태그 이후의 호환성 파손 점검:

`roave-backward-compatibility-check --from={{git_레퍼런스}}`

- 마지막 태그와 특정 참조 간의 호환성 파손 점검:

`roave-backward-compatibility-check --to={{git_레퍼런스}}`

- 호환성 파손 점검 결과를 Markdown으로 출력:

`roave-backward-compatibility-check --format=markdown > {{결과.md}}`
