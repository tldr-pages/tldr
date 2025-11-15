# virt-install

> libvirt를 사용하여 가상 머신을 생성하고 OS 설치를 시작합니다.
> 더 많은 정보: <https://manned.org/virt-install>.

- 1 GB RAM과 12 GB 스토리지를 가진 가상 머신을 생성하고 Debian 설치 시작:

`virt-install --name {{가상머신_이름}} --memory {{1024}} --disk path={{경로/대상/이미지.qcow2}},size={{12}} --cdrom {{경로/대상/debian.iso}}`

- x86-64, KVM 가속, UEFI 기반, Q35 칩셋을 사용하는 가상 머신을 4 GiB RAM, 16 GiB RAW 스토리지와 함께 생성하고 Fedora 설치 시작:

`virt-install --name {{가상머신_이름}} --arch {{x86_64}} --virt-type {{kvm}} --machine {{q35}} --boot {{uefi}} --memory {{4096}} --disk path={{경로/대상/이미지.raw}},size={{16}} --cdrom {{경로/대상/fedora.iso}}`

- 디스크 없이 사운드 장치나 USB 컨트롤러가 없는 라이브 가상 머신 생성. 설치를 시작하지 않고 콘솔에 자동 연결하지 않지만 cdrom을 연결 (tails와 같은 라이브 CD 사용 시 유용할 수 있음):

`virt-install --name {{가상머신_이름}} --memory {{512}} --disk {{none}} --controller {{type=usb,model=none}} --sound {{none}} --autoconsole {{none}} --install {{no_install=yes}} --cdrom {{경로/대상/tails.iso}}`

- 16 GiB RAM, 250 GiB 스토리지, 하이퍼스레딩이 있는 8 코어, 특정 CPU 토폴로지 및 호스트 CPU와 대부분의 기능을 공유하는 CPU 모델을 가진 가상 머신 생성:

`virt-install --name {{가상머신_이름}} --cpu {{host-model}},topology.sockets={{1}},topology.cores={{4}},topology.threads={{2}} --memory {{16384}} --disk path={{경로/대상/이미지.qcow2}},size={{250}} --cdrom {{경로/대상/debian.iso}}`

- Fedora 35를 기반으로 한 자동 배포를 시작하고 원격 리소스만 사용하여 가상 머신 생성 (ISO 불필요):

`virt-install --name {{가상머신_이름}} --memory {{2048}} --disk path={{경로/대상/이미지.qcow2}},size={{20}} --location={{https://download.fedoraproject.org/pub/fedora/linux/releases/35/Everything/x86_64/os/}} --extra-args="{{inst.ks=https://경로/대상/유효한/kickstart.org}}"`
