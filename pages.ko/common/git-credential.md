# git credential

> 사용자 자격 증명을 검색하고 저장.
> 더 많은 정보: <https://git-scm.com/docs/git-credential>.

- 자격 증명 정보를 표시하고, 구성 파일에서 사용자 명과 비밀번호를 검색:

`echo "{{url=http://example.com}}" | git credential fill`

- 모든 구성된 자격 증명 도우미에 자격 증명 정보를 보내서 나중에 사용할 수 있도록 저장:

`echo "{{url=http://example.com}}" | git credential approve`

- 모든 구성된 자격 증명 도우미에서 지정된 자격 증명 정보를 삭제:

`echo "{{url=http://example.com}}" | git credential reject`
