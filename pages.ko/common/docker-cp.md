# docker cp

> 호스트와 컨테이너 파일 시스템 간에 파일이나 디렉토리를 복사.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/cp/>.

- 호스트에서 컨테이너로 파일이나 디렉토리 복사:

`docker cp {{호스트의/파일_또는_디렉토리_경로}} {{컨테이너_이름}}:{{컨테이너의/파일_또는_디렉토리_경로}}`

- 컨테이너에서 호스트로 파일이나 디렉토리 복사:

`docker cp {{컨테이너_이름}}:{{컨테이너의/파일_또는_디렉토리_경로}} {{호스트의/파일_또는_디렉토리_경로}}`

- 호스트에서 컨테이너로 심볼릭 링크를 따라 파일이나 디렉토리 복사 (심볼릭 링크가 아닌 링크된 파일을 직접 복사):

`docker cp --follow-link {{호스트의/심볼릭_링크_경로}} {{컨테이너_이름}}:{{컨테이너의/파일_또는_디렉토리_경로}}`