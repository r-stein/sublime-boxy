> We have no plans to add new themes, only the fixes and improvements to the existing ones.

## Git Commit Guidelines

We have very precise rules over how our git commit messages can be formatted. This leads to more readable messages that are easy to follow when looking through the project history. But also, we use the git commit messages to generate the **Boxy** change log. 

We use [**Angular JS commit guidelines**](https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#-git-commit-guidelines) (except the scope notes, we don't need them).

## Building

These themes use a custom Gulp builder. If you want to edit them you must install it first:

```bash
$ npm install
```

then run watcher by:

```bash
$ gulp watch
```

You can now edit the source files under `sources` folder that will be compiled (don't edit compiled files, all sources are inside `sources`).

If you'd like to add some rules and styles to the template of the color schemes, please, do it inside `sources\schemes\scheme.YAML-tmTheme`. Run `gulp build:schemes` and then generate `*.tmTheme` files in `schemes` folder with such tool as [PackageDev](https://github.com/SublimeText/PackageDev).

All colors can be found in `sources\settings` folder.
