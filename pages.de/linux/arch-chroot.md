# arch-chroot

> Erweiterter `chroot`-Befehl zur Unterstützung des Arch-Linux-Installationsprozesses.
> Weitere Informationen: <https://man.archlinux.org/man/arch-chroot.8>.

- Starte eine interaktive Shell (Standardmäßig Bash) in einem neuen Root-Verzeichnis:

`arch-chroot {{pfad/zu/neuem/root}}`

- Spezifiziere den Benutzer (nicht der jetzige Benutzer) der die Shell ausführt:

`arch-chroot -u {{anderer_benutzer}} {{pfad/zu/neuem/root}}`

- Führe einen benutzerdefinierten Befehl (anstelle des Standardbefehls Bash) im neuen Root-Verzeichnis aus:

`arch-chroot {{pfad/zu/neuem/root}} {{befehl}} {{befehlsparameter}}`

- Gib die Shell an, die nicht die Standard-Shell Bash ist (in diesem Fall sollte das Paket `zsh` auf dem Zielsystem installiert worden sein):

`arch-chroot {{pfad/zu/neuem/root}} {{zsh}}`
