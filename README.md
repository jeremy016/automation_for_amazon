# automation_for_amazon

Automatic test script on amazon

## Requirements

* pip
* virtualenv
* python>=3.6


### selenium Grid
	
- Run by docker-compose
```sh
	docker-compose up -d
```
- Scale node
```sh
docker-compose scale chrome=3
docker-compose scale firefox=3
``` 

## Usage

1. Configure virtual environment
	```
		python3 -m venv sbase_env
		source sbase_env/bin/activate
	```

2. 	Install required packages
	```
		pip install -r requirements.txt
	```

3. Setup 
	3.1 *Login account*
		Insert valid account information in "users.py" (path: utils/users.py)

4. Run tests
	4.1 *Run your tests:*
	```
		python3 -m pytest tests/test_login.py
	```
	4.2 *Run your tests with locales:*
	``` 
		python3 -m pytest tests/test_login.py --locale=[zh-tw|en-us]
	```
	4.3 *Run your tests on the Selenium Grid:*
	``` 
		python3 -m pytest tests/test_login.py --server=IP_ADDRESS --port=4444. 
	```


## troubleshooting
1. Q : This version of ChromeDriver only supports Chrome version 77
	```
		# Install chromedriver latest
		sbase install chromedriver latest 
	```