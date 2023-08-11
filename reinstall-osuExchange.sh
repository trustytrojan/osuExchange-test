# check if bin/pip exists
if ! [[ -f bin/pip ]]; then
	# if not, create a venv
	python -m venv .
fi

# uninstall existing osuExchange version
bin/pip uninstall osuExchange -y

# install the newly built wheel
bin/pip install ../osuExchange/dist/*.whl
