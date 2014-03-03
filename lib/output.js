var markit = require('markit');
var unhtml = require('unhtml');
var colors = require('colors');
var config = require('./config');

var TEXT    = config.colors['text'];
var CMD_BG  = config.colors['command-background'] + 'BG';
var CMD_FG  = config.colors['command-foreground'];
var CMD_TOK = config.colors['command-token'];

var allElements = [
  'blockcode', 'blockhtml', 'blockquote', 'codespan', 'emphasis',
  'header', 'hrule', 'image', 'linebreak', 'link', 'list', 'listitem',
  'paragraph', 'strikethrough', 'strong', 'table', 'tablecell', 'tablerow'
];

exports.fromMarkdown = function(markdown) {

  var r = new markit.Renderer();

  // ignore all syntax by default
  allElements.forEach(function(e) {
    r[e] = function() { return ''; }
  });

  // paragraphs just pass through (automatically created by new lines)
  r.paragraph = function(text) {
    return text;
  };

  //
  // High-level description
  //

  r.blockquote = function(text) {
    text = text.replace('\n', '\n  ');
    return '  ' + text[TEXT];
  };

  //
  // Examples
  //

  r.list = function(body, ordered) {
    return '\n\n' + body[TEXT] + '\n';
  }
  
  r.listitem = function(text) {
    return '  - ' + text[TEXT] + '\n';
  };

  r.codespan = function(code, lang) {
    // split the command on tokens
    var parts = code.split(/\{\{(.*?)\}\}/);
    // every second part is a token
    return '  ' + parts.reduce(function(memo, item, i) {
      if (i % 2) return memo + item[CMD_BG][CMD_TOK];
      else       return memo + item[CMD_BG][CMD_FG];
    }, '');
  };

  var rendered = unhtml(markit(markdown, {renderer: r}));
  return '\n' + rendered + '\n';

};
