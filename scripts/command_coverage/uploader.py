import os

from git import Repo

REPO_URL = 'github.com/tldr-pages/tldr'

def upload_file(svg_dom, svg_file):
	# cloning the git repo
	token = os.environ.get('GH_TOKEN')
	assert token is not None
	local_path = os.path.join(os.environ.get('HOME'), 'tldr')
	repo = Repo.clone_from('https://'+token+'@'+REPO_URL, local_path, depth=1)
	assert repo.__class__ is Repo

	# writing the new svg dom to the file
	target_file = os.path.join(local_path, svg_file)
	with open(target_file, 'w') as f:
		f.write(svg_dom.toxml())

	# creating the commit
	repo.index.add([target_file])
	repo.index.commit('[command coverage] - update coverage')

	# pushing the commit to origin
	repo.remotes.origin.push(refspec=None, progress=None, dry_run=True)
