# meshlabserver

> MeshLab 3D 메쉬 처리 소프트웨어의 명령줄 인터페이스.
> 더 많은 정보: <https://manned.org/meshlabserver>.

- STL 파일을 OBJ 파일로 변환:

`meshlabserver -i {{입력.stl}} -o {{출력.obj}}`

- WRL 파일을 OFF 파일로 변환하고 출력 메쉬에 버텍스 및 면 노멀 포함:

`meshlabserver -i {{입력.wrl}} -o {{출력.off}} -om vn fn`

- 사용 가능한 모든 처리 필터 목록을 파일로 덤프:

`meshlabserver -d {{경로/대상/파일}}`

- MeshLab GUI에서 생성된 필터 스크립트를 사용하여 3D 파일 처리 (Filters > Show current filter script > Save Script):

`meshlabserver -i {{입력.ply}} -o {{출력.ply}} -s {{필터_스크립트.mlx}}`

- 필터 스크립트를 사용하여 3D 파일을 처리하고 필터 출력 내용을 로그 파일에 기록:

`meshlabserver -i {{입력.x3d}} -o {{출력.x3d}} -s {{필터_스크립트.mlx}} -l {{로그파일}}`
