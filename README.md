# Linguist-Demo

This repo contains a GitHub Action that can be run to check the [`github-linguist`](https://github.com/github-linguist/linguist) output for any public repo.

## How to use

To try the demo yourself, follow these steps:

- Create a new repo by clicking **`Use this template`** then **`Create a new repository`** in the top-right corner of the screen (you can even make it private if you prefer).
- Start the workflow to run github-linguist (see image below).

![image](https://github.com/user-attachments/assets/288ad401-74e0-451b-806d-babfe7b72743)

For the slug, it is made of the User_Name (owner) and Repo_Name (name of the repo). You can also just copy paste the URL of the repo there and the excess URL part at the start will be ignored.

Once you’ve started the workflow, it may take a few seconds to appear on the page—you can refresh to see it show up. Click on it to view the progress. 

The results you are looking for will be in the "Run Linguist" step.

![image](https://github.com/user-attachments/assets/1b3d20ad-a0ae-427f-a4ab-d3ad8808ed20)


Example output:
```
Run REPO_NAME=$(echo "github-linguist/linguist" | cut -d'/' -f2)
linguist
68.78%  304730     Ruby
21.95%  97265      C
6.23%   27621      Go
1.57%   6948       Lex
1.18%   5248       Shell
0.28%   1258       Dockerfile

Dockerfile:
.devcontainer/Dockerfile
Dockerfile
tools/grammars/Dockerfile

Shell:
.devcontainer/onCreateCommand.sh
script/add-grammar
script/bootstrap
script/build-grammars-tarball
script/cibuild
script/grammar-compiler
tools/grammars/docker/build

Ruby:
Brewfile
Gemfile
Rakefile
bin/git-linguist
bin/github-linguist
ext/linguist/extconf.rb
github-linguist.gemspec
lib/linguist.rb
lib/linguist/blob.rb
lib/linguist/blob_helper.rb
lib/linguist/classifier.rb
lib/linguist/file_blob.rb
lib/linguist/generated.rb
lib/linguist/grammars.rb
lib/linguist/heuristics.rb
lib/linguist/language.rb
lib/linguist/lazy_blob.rb
lib/linguist/repository.rb
lib/linguist/samples.rb
lib/linguist/sha256.rb
lib/linguist/shebang.rb
lib/linguist/source/diff.rb
lib/linguist/source/repository.rb
lib/linguist/source/rugged.rb
lib/linguist/strategy/extension.rb
lib/linguist/strategy/filename.rb
lib/linguist/strategy/manpage.rb
lib/linguist/strategy/modeline.rb
lib/linguist/strategy/xml.rb
lib/linguist/tokenizer.rb
lib/linguist/version.rb
script/cross-validation
script/fast-submodule-update
script/list-grammars
script/normalise-url
script/sort-submodules
script/update-ids
test/helper.rb
test/test_blob.rb
test/test_classifier.rb
test/test_file_blob.rb
test/test_generated.rb
test/test_grammars.rb
test/test_heuristics.rb
test/test_instrumentation.rb
test/test_language.rb
test/test_pedantic.rb
test/test_repository.rb
test/test_samples.rb
test/test_sha256.rb
test/test_strategies.rb
test/test_tokenizer.rb

C:
ext/linguist/lex.linguist_yy.c
ext/linguist/lex.linguist_yy.h
ext/linguist/linguist.c

Lex:
ext/linguist/tokenizer.l

Go:
tools/grammars/cmd/grammar-compiler/main.go
tools/grammars/compiler/converter.go
tools/grammars/compiler/cson.go
tools/grammars/compiler/data.go
tools/grammars/compiler/errors.go
tools/grammars/compiler/loader.go
tools/grammars/compiler/loader_fs.go
tools/grammars/compiler/loader_url.go
tools/grammars/compiler/pcre.go
tools/grammars/compiler/pcre_test.go
tools/grammars/compiler/proto.go
tools/grammars/compiler/walker.go
tools/grammars/pcre/pcre.go
```
