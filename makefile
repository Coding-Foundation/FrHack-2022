lab:
	jupyter-lab --ip 0.0.0.0 --collaborative --allow-root
front-install:
	npm --prefix anfr-front install
front:
	npm --prefix anfr-front start
