# Brief guide on how to set up a Python environment in MacOS
No comments, just a list of steps to follow.
Assuming you have Homebrew installed, and you are using zsh. For bash, replace `.zshrc` with `.bashrc`.

- install `pyenv` + `pyenv-virtualenv`
	- [ ] `brew install pyenv`
	- [ ] `brew install pyenv-virtualenv`
	- [ ] `echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc`
	- [ ] `source ~/.zshrc`
- create global Python version
	- [ ] see available versions: `pyenv install --list`
		- I decide I go for the latest 3.10 - just because I've been using it for a while
	- [ ] `pyenv install 3.10.14`
- create local env named "mlz"
	- [ ] `pyenv virtualenv 3.10.14 mlz`
    - [ ] `pyenv local mlz`

It turned out to somehow conflict with my Mamba, but in VS Code I can still select the Python interpreter to be the one from the virtual environment. So I guess it's fine.