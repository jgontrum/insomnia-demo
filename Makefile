.PHONY: clean start build-docker start-docker attach-to-docker

all: env/bin/python

env/bin/python:
	virtualenv env -p python3.5 --no-site-packages
	env/bin/pip install --upgrade pip
	env/bin/pip install wheel
	env/bin/pip install -r requirements.txt
	env/bin/python setup.py develop

clean:
	rm -rfv bin develop-eggs dist downloads eggs env parts
	rm -fv .DS_Store .coverage .installed.cfg bootstrap.py
	rm -fv logs/*.txt
	find . -name '*.pyc' -exec rm -fv {} \;
	find . -name '*.pyo' -exec rm -fv {} \;
	find . -depth -name '*.egg-info' -exec rm -rfv {} \;
	find . -depth -name '__pycache__' -exec rm -rfv {} \;

build-docker: clean
	docker build -t jgontrum/insomnia_demo_api .

start-docker:
	mkdir -p /tmp/insomnia_demo_api-logs
	docker rm insomnia_demo_api || true
	docker run --name "insomnia_demo_api" -p "127.0.0.1:50001:50001" -v "/tmp/insomnia_demo_api-logs:/app/logs" jgontrum/insomnia_demo_api

attach-to-docker:
	 docker exec -i -t insomnia_demo_api /bin/bash 

start: env/bin/python
	env/bin/uwsgi --yaml=config/uwsgi.yml

