install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C,W app.py

build:
	docker build -t us-west1-docker.pkg.dev/garbage-classfication/garbage-classify-repo/hello-app:latest .

run:
	docker run --rm -p 8080:8080 us-west1-docker.pkg.dev/garbage-classfication/garbage-classify-repo/hello-app:latest

all: install lint
