# docker node

> Docker Swarm의 노드를 관리.
> 더 많은 정보: <https://docs.docker.com/reference/cli/docker/node/>.

- Swarm에 속한 노드 목록 출력:

`docker node ls`

- 하나 이상의 노드에서 실행 중인 작업 목록 출력 (기본값: 현재 노드):

`docker node ps {{노드1 노드2 노드3 ...}}`

- 하나 이상의 노드에 대한 상세 정보 출력:

`docker node inspect {{노드1 노드2 노드3 ...}}`

- 하나 이상의 노드를 Swarm의 매니저로 승격:

`docker node promote {{노드1 노드2 노드3 ...}}`

- 하나 이상의 노드를 Swarm 내 매니저에서 일반 노드로 강등 :

`docker node demote {{노드1 노드2 노드3 ...}}`

- 하나 이상의 노드를 Swarm에서 제거:

`docker node rm {{노드1 노드2 노드3 ...}}`

- 노드의 메타데이터(가용성, 라벨, 역할 등) 업데이트:

`docker node update --{{availability|role|label-add|...}} {{active|worker|...}} {{노드1}}`
