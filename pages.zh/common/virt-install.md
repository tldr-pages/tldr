# virt-install

> 使用 libvirt 创建虚拟机并开始操作系统安装。
> 更多信息：<https://virt-manager.org/>.

- 创建一个具有 1 GB 内存和 12 GB 存储的虚拟机，并开始 Debian 安装：

`virt-install --name {{vm_name}} --memory {{1024}} --disk path={{path/to/image.qcow2}},size={{12}} --cdrom {{path/to/debian.iso}}`

- 创建一个基于 Q35 芯片组的 x86-64、KVM 加速、UEFI 的虚拟机，具有 4 GiB 内存、16 GiB RAW 存储，并开始 Fedora 安装：

`virt-install --name {{vm_name}} --arch {{x86_64}} --virt-type {{kvm}} --machine {{q35}} --boot {{uefi}} --memory {{4096}} --disk path={{path/to/image.raw}},size={{16}} --cdrom {{path/to/fedora.iso}}`

- 创建一个无盘的实时虚拟机，不带模拟的声卡或 USB 控制器。不要启动安装，也不要自动连接到控制台，但附加一个 cdrom（在使用像 tails 这样的实时 CD 时可能有用）：

`virt-install --name {{vm_name}} --memory {{512}} --disk {{none}} --controller {{type=usb,model=none}} --sound {{none}} --autoconsole {{none}} --install {{no_install=yes}} --cdrom {{path/to/tails.iso}}`

- 创建一个具有 16 GiB 内存、250 GiB 存储、8 个核心（支持超线程）、特定 CPU 拓扑以及与主机 CPU 共享大部分特性的 CPU 模型的虚拟机：

`virt-install --name {{vm_name}} --cpu {{host-model}},topology.sockets={{1}},topology.cores={{4}},topology.threads={{2}} --memory {{16384}} --disk path={{path/to/image.qcow2}},size={{250}} --cdrom {{path/to/debian.iso}}`

- 创建一个虚拟机并通过仅使用远程资源（不需要 ISO）启动基于 Fedora 35 的自动部署：

`virt-install --name {{vm_name}} --memory {{2048}} --disk path={{path/to/image.qcow2}},size={{20}} --location={{https://download.fedoraproject.org/pub/fedora/linux/releases/35/Everything/x86_64/os/}} --extra-args="{{inst.ks=https://path/to/valid/kickstart.org}}"`