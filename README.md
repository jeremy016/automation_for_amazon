# automation_for_amazon

Automatic test script on amazon

## Requirements

* pip
* virtualenv
* python>=3.6


## Usage

1. Configure virtual environment
	```
	$ python3 -m venv sbase_env
	$ source sbase_env/bin/activate
	```

2. 	Install required packages
	```
	$ pip install requirements.txt
	```

3. Run case
	```
	$ python3 -m pytest cases/test_create_comment.py -k "test_create_comment_with_pure_text" --html=report/report.html
	```
