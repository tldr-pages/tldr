# nixos-rebuild

> Reconfigurați o mașină NiXOS.
> Mai multe informaţii: <https://nixos.org/nixos/manual/#sec-changing-config>

- Construiți și comutați la noua configurație, făcându-l implicit de boot:

`sudo nixos-rebuild switch`

- Construiți și treceți la noua configurație, făcându-l implicit de boot și numind intrarea de boot:

`sudo nixos-rebuild switch -p {{name}}`

- Construiți și comutați la noua configurație, făcându-l implicit de boot și instalarea actualizărilor:

`sudo nixos-rebuild switch --upgrade`

- Modificări de revenire la configurație, trecerea la generația anterioară:

`sudo nixos-rebuild switch --rollback`

- Construiți noua configurație și faceți-o implicit de boot fără a comuta la ea:

`sudo nixos-rebuild boot`

- Construiți și activați noua configurație, dar nu faceți o intrare de boot (în scopuri de testare):

`sudo nixos-rebuild test`

- Construiți configurația și deschideți-o într-o mașină virtuală:

`sudo nixos-rebuild build-vm`
