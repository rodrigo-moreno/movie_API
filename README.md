# Movie API

Movie API designed to interact with *VLC* player in an _HTPC_ for Gamma 46 community

## Installation of development environment
* Required `python 3.8.5`
* Create a virtual environment with 
	```
	python -m venv venv
	```
* Activate such environment using 
	```
	source venv/bin/activate
	```
* Install required packages
	```
	pip install -r requirements.txt
	```
* Add environment variables for flask 
	```
	export FLASK_APP=minimal.py
	export FLASK_ENV=development
	```
* Run web server
	```
	flask run
	```