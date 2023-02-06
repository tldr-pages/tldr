# cpupower

> CPU teljesítményre és tuning lehetőségekre vonatkozó eszközök. Ez a parancs elérhető a `cpupower` csomag részeként, vagy a Fedora rendszeren a `kernel-tools` részeként. További információ: <https://manned.org/cpupower>.

- CPU-k listázása:

`sudo cpupower --cpu {{all}} info`

- Az összes processzormagra vonatkozó információk kinyomtatása:

`sudo cpupower --cpu {{all}} info`

- Az összes CPU-t energiatakarékos frekvenciakormányzóra állítja:

`sudo cpupower --cpu {{all}} frequency-set --governor {{powersave}}`

- A CPU 0 rendelkezésre álló frekvencia \[g\]overnorok nyomtatása:

`sudo cpupower --cpu {{0}} frequency-info g | grep "analyzing\|governors"`

- A CPU 4 frekvenciájának nyomtatása a hardverről, ember által olvasható formátumban:

`sudo cpupower --cpu {{4}} frequency-info --hwfreq --human`
