'use strict';

var glob = require('glob');

function parsePlatform(pagefile) {
  return pagefile.split(/\//)[1];
}

function parsePagename(pagefile) {
  return pagefile.split(/\//)[2].replace(/\.md$/, '');
}

function parseLanguage(pagefile) {
  var pagesFolder = pagefile.split(/\//)[0];
  return pagesFolder == 'pages' ? 'en' : pagesFolder.replace(/^pages./, '');
}

function buildPagesIndex(files) {
  var reducer = function (index, file) {
    var os = parsePlatform(file);
    var page = parsePagename(file);
    var language = parseLanguage(file);
    if (index[page]) {
      if (!index[page].platform.includes(os))
        index[page].platform.push(os);
      index[page].language.push(language);
    } else {
      index[page] = {name: page, platform: [os], language: [language]};
    }
    return index;
  };

  return Object.values(files.reduce(reducer, {}));
}

function saveIndex(index) {
  var indexFile = {
    commands: index
  };
  console.log(JSON.stringify(indexFile));
}

glob('pages*/**/*.md', function (er, files) {
  var index = buildPagesIndex(files);
  saveIndex(index);
});
