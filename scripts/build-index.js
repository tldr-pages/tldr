'use strict';

const glob = require('glob');

function parsePlatform(pagefile) {
  return pagefile.split(/\//)[1];
}

function parsePagename(pagefile) {
  return pagefile.split(/\//)[2].replace(/\.md$/, '');
}

function parseLanguage(pagefile) {
  let pagesFolder = pagefile.split(/\//)[0];
  return pagesFolder == 'pages' ? 'en' : pagesFolder.replace(/^pages\./, '');
}

function buildPagesIndex(files) {
  let reducer = function (index, file) {
    let os = parsePlatform(file);
    let page = parsePagename(file);
    let language = parseLanguage(file);

    if (index[page]) {
      let targets = index[page].targets;
      let needsPush = true;
      for (const target of targets) {
        if (target.platform === os && target.language === language) {
          needsPush = false;
          continue
        }
      }
      if (needsPush) {
        targets.push({"os": os, "language": language})
        index[page].targets = targets;
      }
    } else {
      index[page] = {name: page, targets: [{"os": os, "language": language}]};
    }

    return index;
  };

  let obj = files.reduce(reducer, {});

  return Object.keys(obj)
      .sort()
      .map(function(page) {
        return {
          name: page,
          targets: obj[page]["targets"]
        };
      });
}

function saveIndex(index) {
  let indexFile = {
    commands: index
  };

  console.log(JSON.stringify(indexFile));
}

glob('pages*/**/*.md', function (er, files) {
  if (er !== null) {
    console.error('ERROR finding pages!');
    console.error(er);
    return;
  }

  let index = buildPagesIndex(files);
  saveIndex(index);
});
