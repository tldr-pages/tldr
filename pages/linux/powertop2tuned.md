# powertop2tuned

> Create TuneD profiles from PowerTOP recommendations.
> Part of `tuned-utils`.
> See also: `powertop`, `tuned-adm`.
> More information: <https://docs.fedoraproject.org/en-US/quick-docs/automatic-power-management-power2top/>.

- Create a new TuneD profile based on current PowerTOP recommendations:

`sudo powertop2tuned {{profile_name}}`

- Create a new profile and enable most recommendations automatically:

`sudo powertop2tuned {{[-e|--enable]}} {{profile_name}}`

- Create a profile from an existing PowerTOP HTML report:

`sudo powertop2tuned {{[-i|--input]}} {{path/to/report.html}} {{profile_name}}`

- Create a new profile in a specific directory:

`sudo powertop2tuned {{[-o|--output]}} {{path/to/directory}} {{profile_name}}`

- Create a new profile without merging the active profile:

`sudo powertop2tuned {{[-n|--new-profile]}} {{profile_name}}`

- Merge recommendations with a specific existing profile:

`sudo powertop2tuned {{[-m|--merge-profile]}} {{existing_profile}} {{profile_name}}`

- Force overwrite an existing profile directory:

`sudo powertop2tuned {{[-f|--force]}} {{profile_name}}`
