var fs        = require('fs');
var path      = require('path');
var async     = require('async');
var mkdirp    = require('mkdirp');
var rmdir     = require('rimraf');
var config    = require('./config');
var request   = require('./request');

exports.get = function(filename, done) {
  var filepath = path.join(config.local.cacheFolder, filename);
  async.waterfall([
    function(next) { checkCache(filepath, next); },
    function(next) { getContent(filepath, next); }
  ], done);
};

exports.save = function(filename, contents, done) {
  var filepath = path.join(config.local.cacheFolder, filename);
  var dir = path.dirname(filepath);
  mkdirp(dir, function(err) {
    fs.writeFile(filepath, contents, done);
  });
};

exports.clear = function() {
  rmdir(config.local.cacheFolder, function(err) {
    console.log('Cache cleared');
  });
};

exports.update = function(opts) {
  var tags = request.getTags(opts, function(err, tags) {
    var tag = tags[0];
    if (opts.tag) {
      tags.forEach(function(t) {
        if (t.name === opts.tag) {
          tag = t;
        }
      });
    }
    console.log("Updating from " + config.updateRepo + ":" + tag.name);
    request.getZip(tag.zipball_url, function(err, pth) {
      var subdirs = fs.readdirSync(pth).filter(function(subdir) {
        var stat = fs.statSync(path.resolve(pth, subdir));
        return stat.isDirectory();
      });
      if (!fs.existsSync(config.local.cacheFolder)) {
        fs.mkdirSync(config.local.cacheFolder);
      }
      var mds = fs.readdirSync(path.resolve(pth, subdirs[0]));
      mds.forEach(function(md) {
        if (path.extname(md) === '.md') {
          var npath = path.resolve(config.local.cacheFolder, md),
              opath = path.resolve(pth, subdirs[0], md);
          if (fs.existsSync(npath)) {
            fs.unlinkSync(npath);
          }
          copyFile(opath, npath, function(err) {
            if (err)
              console.log("ERR: " + err);
          });
        }
      });
    });
  });
}

function checkCache(filepath, done) {
  fs.stat(filepath, function(err, stat) {
    if (err) {
      done("'" + path.basename(filepath).replace(/\..*\.md$/,"") + "' not found. Try updating from the server with the --update flag, or contributing a pull request to https://github.com/rprieto/tldr");
    } else {
      done(null);
    }
  });
}

function getContent(filepath, done) {
  fs.readFile(filepath, function (err, contents) {
    if (err) {
      done(path.basename(filepath) + " not found. Try updating from the server with the --update flag, or contributing Pull Request to https://github.com/rprieto/tldr");
    } else {
      done(null, contents.toString());
    }
  });
}

function copyFile(source, target, cb) {
  var cbCalled = false,
    rd = fs.createReadStream(source),
    wr = fs.createWriteStream(target);
  rd.on("error", function(err) {
    done(err);
  });
  wr.on("error", function(err) {
    done(err);
  });
  wr.on("close", function(ex) {
    done();
  });
  rd.pipe(wr);

  var done = function(err) {
    if (!cbCalled) {
      cb(err);
      cbCalled = true;
    }
  };
}

