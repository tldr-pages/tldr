# virt-install

> Virtuális gépek létrehozása a libvirt segítségével és az operációs rendszer telepítésének megkezdése. További információ: <https://virt-manager.org/>.

- Hozzon létre egy virtuális gépet 1 GB RAM-mal és 12 GB tárhellyel, és indítsa el a Debian telepítését:

`virt-install --name {{vm_name}} --memory {{1024}} --disk path={{path/to/image.qcow2}},size={{12}} --cdrom {{path/to/debian.iso}}`

- Hozzon létre egy x86-64-es, KVM-gyorsított, UEFI-alapú virtuális gépet Q35 lapkakészlettel, 4 GiB RAM-mal, 16 GiB RAW-tárolóval, és indítson el egy Fedora telepítést:

`virt-install --name {{vm_name}} --arch {{x86_64}} --virt-type {{kvm}} --machine {{q35}} --boot {{uefi}} --memory {{4096}} --disk path={{path/to/image.raw}},size={{16}} --cdrom {{path/to/fedora.iso}}`

- Hozzon létre egy lemez nélküli élő virtuális gépet emulált hangeszköz vagy USB-vezérlő nélkül. Ne indítson telepítést, és ne csatlakozzon automatikusan a konzolhoz, hanem csatoljon hozzá egy cdrom-ot (hasznos lehet, ha élő CD-t használ, mint a tails):

`virt-install --name {{vm_name}} --memory {{512}} --disk {{none}} --controller {{type=usb,model=none}} --sound {{none}} --autoconsole {{none}} --install {{no_install=yes}} --cdrom {{path/to/tails.iso}}`

- Hozzon létre egy virtuális gépet 16 GiB RAM-mal, 250 GiB tárolóval, 8 maggal hyperthreadinggel, egy speciális CPU-topológiával és egy olyan CPU-modellel, amely a legtöbb funkciót megosztja a host CPU-val:

`virt-install --name {{vm_name}} --cpu {{host-model}},topology.sockets={{1}},topology.cores={{4}},topology.threads={{2}} --memory {{16384}} --disk path={{path/to/image.qcow2}},size={{250}} --cdrom {{path/to/debian.iso}}`

- Hozzon létre egy virtuális gépet, és indítson el egy automatikus telepítést a Fedora 35 alapján, csak távoli erőforrások felhasználásával (ISO nem szükséges):

`virt-install --name {{vm_name}} --memory {{2048}} --disk path={{path/to/image.qcow2}},size={{20}} --location={{https://download.fedoraproject.org/pub/fedora/linux/releases/35/Everything/x86_64/os/}} --extra-args={{"inst.ks=https://path/to/valid/kickstart.org"}}`
