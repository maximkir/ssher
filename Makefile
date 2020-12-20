PYTHON_VERSION?=3.8.5

black:
	$(VENV)/black --check ssher/


include Makefile.venv
Makefile.venv:
	curl \
		-o Makefile.fetched \
		-L "https://raw.githubusercontent.com/maximkir/python-venv-template/v2020.12.20/Makefile"
	echo "1c79f371eda3c40441efaf59ecb830bd8c6b6f31ae0cac3f772626dcc498ac06 *Makefile.fetched" \
		| sha256sum --check - \
		&& mv Makefile.fetched Makefile.venv
