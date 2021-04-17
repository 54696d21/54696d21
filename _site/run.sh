#!/bin/bash -l
# https://jekyllrb.com/docs/deployment/automated/

# Install Ruby Gems to ~/gems
export GEM_HOME=$HOME/gems
export PATH=$GEM_HOME/bin:$PATH

TMP_GIT_CLONE=$HOME/tmp/myrepo
GEMFILE=$TMP_GIT_CLONE/Gemfile
PUBLIC_WWW=/var/www/myrepo

git clone $GIT_DIR $TMP_GIT_CLONE
BUNDLE_GEMFILE=$GEMFILE bundle install
BUNDLE_GEMFILE=$GEMFILE bundle exec jekyll build -s $TMP_GIT_CLONE -d $PUBLIC_WWW
rm -Rf $TMP_GIT_CLONE
exit
