# esbuild-visualizer

> Visualize and analyze esbuild bundle metadata in an interactive treemap, sunburst, or flamegraph chart.
> More information: <https://github.com/btd/esbuild-visualizer>.

- Generate an interactive HTML bundle report from an esbuild metafile:

`esbuild-visualizer --metadata {{path/to/meta.json}} --filename {{stats.html}}`

- Generate a report using a specific chart template:

`esbuild-visualizer --metadata {{path/to/meta.json}} --template {{treemap|sunburst|network}}`

- Open the generated visualization automatically in the default browser:

`esbuild-visualizer --metadata {{path/to/meta.json}} --open`
