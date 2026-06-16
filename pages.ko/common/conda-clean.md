# conda clean

> 임시 파일 또는 사용되지 않는 파일 삭제(인덱스 캐시, 잠금 파일, 사용되지 않는 캐시 패키지, tarball 및 로그 파일).
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/stable/commands/clean.html>.

- 모든 임시 또는 사용되지 않는 파일을 자세하게 출력을 포함해 삭제 후,모든 확인에 자동으로 yes 응답:

`conda clean {{[-avy|--all --verbose --yes]}}`

- 인덱스 캐시, tarball 및 로그 파일만 삭제:

`conda clean {{[-itl|--index-cache --tarballs --logfiles]}}`

- 이전에 사용 중이어서 삭제되지 못한 임시 캐시([c]ache) 파일만 삭제:

`conda clean {{[-c|--tempfiles]}} {{경로/대상/tempfiles}}`

- 사용되지 않는 패키지만 삭제. (softlink로 설치된 패키지도 삭제될 수 있음):

`conda clean {{[-p|--packages]}}`

- 모든 쓰기 가능한 패키지를 강제로 삭제. `--all` 옵션보다 더 광범위하며, softlink로 설치된 패키지도 삭제됨:

`conda clean {{[-f|--force-pkgs-dirs]}}`

- 도움말 표시:

`conda clean {{[-h|--help]}}`
