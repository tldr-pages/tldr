var request = require('./request');
var cache   = require('./cache');
var os      = require('os');
var async   = require('async');
var fs      = require('fs');
var config  = require('./config');
var path    = require('path');

var osDirectories = {
    darwin  : 'osx',
    linux   : 'linux',
    sunos   : 'sunos'
};

function commandPath(command, platform) {
  return (platform || osDirectories[os.platform()]) + '/' + command + '.md';
}

function getForPlatform(repository, command, platform, done) {
  var pathCommon = commandPath(command, "common");
  var pathPlatform = commandPath(command, platform);

  async.parallel([
    function(callback) {
      repository.get(pathCommon, function() { callback(null, arguments); });
    },
    function(callback) {
      repository.get(pathPlatform, function() { callback(null, arguments); });
    }
  ], function(err, results){
    var errCommon = results[0][0];
    var errPlatform = results[1][0];
    var contentsCommon = results[0][1];
    var contentsPlatform = results[1][1];
    if(errCommon && errPlatform) {
      done(errCommon);
    } else {
      done(null, contentsPlatform || contentsCommon);
    }
  });

}

exports.get = function(command, options, done) {
  options = options || {};
  var resolver = this;
  resolver.getLocal(command, options.os, done);
};

exports.getLocal = function(command, platform, done) {
  getForPlatform(cache, command, platform, done);
};

exports.getRemote = function(command, platform, done) {
  getForPlatform(request, command, platform, done);
};

exports.list = function() {
  var fileList = getFileList();
  for (dir in fileList) {
    console.log((dir[dir.length - 1] === '/' ? dir : dir+'/'));
    fileList[dir].forEach(function(file) {
      console.log('\t'+file);
    });
  }
};

exports.getRandom = function() {
  var fileList = getFileList();
  var allFiles = [];
  for (dir in fileList) {
    if (applicableDir(dir))
      allFiles = allFiles.concat(fileList[dir]);
  }
  return allFiles[Math.floor(Math.random()*allFiles.length)];
};

function applicableDir(dir) {
  return dir === 'common' || dir === osDirectories[os.platform()];
};

function getFileList() {
  var retval = {};
  var files = fs.readdirSync(config.local.cacheFolder);
  files.forEach(function(file) {
    var fullpath = path.join(config.local.cacheFolder, file);
    var stat = fs.statSync(fullpath);
    if (stat.isDirectory()) {
      var subfiles = fs.readdirSync(fullpath).filter(function(subfile) {
        return path.extname(subfile) === '.md';
      }).map(function(subfile) {
        return subfile.replace(/\.md$/, "");
      });
      retval[file] = subfiles;
    }
  });
  return retval;
};
