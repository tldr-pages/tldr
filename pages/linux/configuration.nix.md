# configuration.nix

> NixOS declarative system configuration of your NixOS system.
> `nixos-rebuild` applies this configuration.
> More information: <https://nixos.org/manual/nixos/stable/#ch-configuration>

- Specify which packages you want on your system.

`{ environment.systemPackages = [ pkgs.neovim ]; }`

- Enable X11 for GUI:

`{ services.xserver.enable = true; }`

- To enable a wayland compositor like sway or hyprland with essential utilities:

`{ programs.sway.enable = true; }`

- To enable a desktop environment such as gnome or kde:

`{ services.xserver.desktopManager.gnome.enable = true; }`

- To enable a window manager such as xmonad or i3:

`{ services.xserver.windowManager.xmonad.enable = true; }`

- To enable NetworkManager:

`{ networking.networkmanager.enable = true; }`

- To switch to the latest kernel:

`{ boot.kernelPackages = pkgs.linuxPackages_latest; }`
