# dircolors

> Geef commando's weer om de LS_COLOR-omgevingsvariabele in te stellen en style `ls`, `dir` enz.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>.

- Geef commando's weer om LS_COLOR in te stellen met standaardkleuren:

`dircolors`

- Toon ieder bestandstype met de kleur zoals deze in `ls` getoond zou worden:

`dircolors --print-ls-colors`

- Geef commando's weer om LS_COLOR in te stellen met kleuren uit een bestand:

`dircolors {{pad/naar/bestand}}`

- Geef commando's weer voor de Bourne-shell:

`dircolors {{[-b|--bourne-shell]}}`

- Geef commando's weer voor de C-shell:

`dircolors {{[-c|--c-shell]}}`

- Bekijk de standaardkleuren voor bestandstypen en extensies:

`dircolors {{[-p|--print-database]}}`
