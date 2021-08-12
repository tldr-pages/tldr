# sops

> SOPS: Secretele Operațiuni.
> Instrument pentru gestionarea secretelor.
> Mai multe informaţii: <https://github.com/mozilla/sops>

- Criptează un fișier:

`sops -e {{path/to/myfile.json}} > {{path/to/myfile.enc.json}}`

- Decripta un fișier la ieșirea standard:

`sops -d {{path/to/myfile.enc.json}}`

- Rotiți cheile de date pentru un fișier sops:

`sops -r {{path/to/myfile.enc.yaml}}`

- Modificați extensia fișierului după criptare:

`sops -d --input-type json {{path/to/myfile.enc.json}}`

- Extragerea cheilor prin denumire și elemente matrice prin numerotarea lor:

`sops -d --extract '["an_array"][1]' {{path/to/myfile.enc.json}}`

- Arată diferența dintre două fișiere sops:

`diff <(sops -d {{path/to/secret1.enc.yaml}}) <(sops -d {{path/to/secret2.enc.yaml}})`
