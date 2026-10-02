# gpm

> Linux 가상 콘솔에서 마우스 지원을 활성화.
> 더 많은 정보: <https://manned.org/gpm>.

- PS/2 타입([t]ype) 마우스([m]ouse)를 사용하여 gpm 시작:

`sudo gpm -m /dev/input/mice -t ps2`

- Microsoft 타입([t]ype) 직렬(serial) 마우스([m]ouse)를 사용하여 gpm 시작:

`sudo gpm -m /dev/ttyS0 -t ms`

- 디버깅([D]ebugging)을 위해 포그라운드에서 지정한 마우스([m]ouse)와 유형([t]ype)으로 gpm 시작:

`sudo gpm -m {{경로/대상/마우스_장치}} -t {{마우스_타입}} -D`

- 실행 중인 gpm 종료([k]ill):

`sudo gpm -k`

- 서버 호환성을 위한 리피터([R]epeater) 모드로 마우스([m]ouse)와 유형([t]ype)으로 gpm 시작 :

`sudo gpm -m {{경로/대상/마우스_장치}} -t {{마우스_타입}} -R`

- 사용 가능한 마우스 유형([t]ypes) 목록 표시:

`gpm -t help`
