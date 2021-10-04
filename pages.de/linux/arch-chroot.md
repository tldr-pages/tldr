# arch-chroot

> Erweiterter `chroot`-Befehl zur Unterstützung des Arch Linux-Installationsprozesses.
> Weitere Informationen: <https://man.archlinux.org/man/arch-chroot.8>.

- Starte eine interaktive Shell (`bash` ist der Standard) in einem neuen Root-Verzeichnis:

`arch-chroot {{pfad/zum/neuen/root}}`

- Spezifiziere den Benutzer (nicht der jetzige Benutzer) der die Shell ausführt:

`arch-chroot -u {{anderer_benutzer}} {{pfad/zum/neuen/root}}`

- Führe einen benutzerdefinierten Befehl (anstelle des Standardbefehls `bash`) im neuen Root-Verzeichnis aus:

`arch-chroot {{pfad/zum/neuen/root}} {{befehl}} {{befehlsparameter}}`

- Gebe die Shell an, die nicht die Standard-Shell `bash` ist (in diesem Fall sollte das Paket `zsh` auf dem Zielsystem installiert worden sein):

`arch-chroot {{pfad/zum/neuen/root}} {{zsh}}`
