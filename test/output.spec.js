var should = require('should');
var colors = require('ansicolors');
var output = require('../lib/output');

describe('Console output from Markdown', function() {

  it('surrounds the output with blank lines', function() {
    var o = output.fromMarkdown('');
    o.should.eql('\n\n');
  });
    
  it('strips paragraph tags', function() {
    var o = output.fromMarkdown(
      '\nline 1' +
      '\n' +
      '\nline 2' +
      '\n'
    );
    o.should.eql('\nline 1line 2\n');
  });

  it('reads the command description from block quotes', function() {
    var o = output.fromMarkdown(
      '\n> archiving utility' +
      '\n> supports optional compression'
    );
    o.should.include('archiving utility');
    o.should.include('supports optional compression');
    o.should.startWith('\n  \u001b[3m');
    o.should.endWith('\u001b[23m\n');
  });
  
  it('ignores all other Markdown syntax', function() {
    var o = output.fromMarkdown(
      '\n# heading 1' +
      '\n' +
      '\n## heading 2' +
      '\n' +
      '\n[link](http://link)' +
      '\n' +
      '\n```' +
      '\ncode block' +
      '\n```'
    );
    o.should.eql('\n\n');
  });

  it('highlights replaceable {{tokens}}', function() {
    var o = output.fromMarkdown('`hello {{token}} bye`');
    o.should.include(
      colors.open.red   + 'hello ' +
      colors.open.white + 'token'  +
      colors.open.red   + ' bye');
  });

});
