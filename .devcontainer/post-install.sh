#!/bin/bash
set -ex

##
## Create some aliases
##
echo 'alias ll="ls -alF"' >> $HOME/.bashrc
echo 'alias la="ls -A"' >> $HOME/.bashrc
echo 'alias l="ls -CF"' >> $HOME/.bashrc

# Convenience workspace directory for later use
WORKSPACE_DIR=$(pwd)

##
## Python project configuration & deps
##

# Change some Poetry settings to better deal with working in a container
poetry config cache-dir ${WORKSPACE_DIR}/.cache
poetry config virtualenvs.in-project true

# Now install all dependencies
poetry install

echo "Done!"
