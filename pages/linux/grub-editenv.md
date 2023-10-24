# `grub-editenv` - Edit GRUB Environment Variables

`grub-editenv` is a command-line tool that allows you to manipulate environment variables in the GRUB bootloader configuration. It provides a simpler and more approachable way to edit these variables compared to traditional GRUB configuration files.

## Usage
grub-editenv [OPTION] VARNAME=VALUE


## Options

- `-h, --help`: Show help message and exit.

## Examples

1. **Set Timeout Value:**
   To set the timeout value for GRUB to 5 seconds, use the following command:
   ```bash
   grub-editenv TIMEOUT=5
   ```

2. **Enable Debug Mode:** 
    To enable debugging in GRUB, you can set the GRUB_CMDLINE_LINUX variable:
   ```bash
   grub-editenv GRUB_CMDLINE_LINUX="debug"
   ```