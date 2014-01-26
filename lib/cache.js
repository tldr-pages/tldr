var fs     = require('fs');
var os     = require('os');
var path   = require('path');
var async  = require('async');
var mkdirp = require('mkdirp');
var config  = require('./config');

var FOLDER = path.join(os.tmpdir ? os.tmpdir() : os.tmpDir(), 'tldr-cache');

exports.get = function(filename, done) {
  var filepath = path.join(FOLDER, filename);
  async.waterfall([
    function(next) { checkCache(filepath, next); },
    function(next) { getContent(filepath, next); }
  ], done);
};

exports.save = function(filename, contents, done) {
  mkdirp(FOLDER, function(err) {
    var filepath = path.join(FOLDER, filename);
    fs.writeFile(filepath, contents, done);
  });
};

function checkCache(filepath, done) {
  fs.stat(filepath, function(err, stat) {
    if (err) {
      done('cache miss: ' + filepath);
    } else {
      var age = (new Date().getTime() - stat.mtime.getTime()) / 1000;
      if (age > config.remote.maxAge) {
        done('cache too old:' + filepath);
      } else {
        done(null);
      }
    }
  });
}

function getContent(filepath, done) {
  fs.readFile(filepath, function (err, contents) {
    if (err) {
      done('cache miss: ' + filepath);
    } else {
      done(null, contents.toString());
    }
  });
}
