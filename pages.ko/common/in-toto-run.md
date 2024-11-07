# in-toto-run

> 공급망 단계를 수행하는 동안 링크 메타데이터를 생성.
> 더 많은 정보: <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-run.html>.

- Git 저장소에 태그를 지정하고 결과 링크 파일에 서명:

`in-toto-run -n {{tag}} --products {{.}} -k {{키_파일}} -- {{git tag v1.0}}`

- 파일을 재료로 저장하고, 타르볼을 제품으로 저장하여 타르볼을 생성:

`in-toto-run -n {{패키지}} -m {{프로젝트}} -p {{프로젝트.tar.gz}} -- {{tar czf 프로젝트.tar.gz project}}`

- 검토 작업을 위해 서명된 증명을 생성:

`in-toto-run -n {{리뷰}} -k {{키_파일}} -m {{document.pdf}} -x`

- Trivy를 사용하여 이미지를 스캔하고 링크 파일을 생성:

`in-toto-run -n {{스캔}} -k {{키_파일}} -p {{리포트.json}} -- {{/bin/sh -c "trivy -o report.json -f json <IMAGE>"}}`
