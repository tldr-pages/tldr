# in-toto-run

> 공급망 단계 수행과 동시에 링크 메타데이터를 생성하는 도구.
> 더 많은 정보: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-run.html>.

- Git 저장소에 태그를 생성하고 링크 파일에 서명:

`in-toto-run {{[-n|--step-name]}} {{태그}} {{[-p|--products]}} {{.}} --signing-key {{키_파일}} -- {{git tag v1.0}}`

- tarball을 생성하고, 원본 파일은 materials로, 생성된 tarball은 product로 기록:

`in-toto-run {{[-n|--step-name]}} {{package}} {{[-m|--materials]}} {{project}} {{[-p|--products]}} {{project.tar.gz}} -- {{tar czf project.tar.gz project}}`

- 리뷰 작업에 대한 서명된 증명 생성:

`in-toto-run {{[-n|--step-name]}} {{review}} --signing-key {{키_파일}} {{[-m|--materials]}} {{문서.pdf}} {{[-x|--no-command]}}`

- Trivy로 이미지를 스캔하고 링크 파일 생성:

`in-toto-run {{[-n|--step-name]}} {{scan}} --signing-key {{키_파일}} {{[-p|--products]}} {{report.json}} -- /bin/sh -c "trivy --output report.json --format json {{경로/대상/이미지}}"`
