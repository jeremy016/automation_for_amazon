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
```sh
python3 -m venv sbase_env
source sbase_env/bin/activate
```

2. 	Install required packages
```sh
pip install -r requirements.txt
```

3. Setup 
	1. Login account
		> Insert a valid account information (path: utils/users.py)
	2. Login email
		> Insert a valid mailosaur email account (path: utils/users.py) (Note: I use *Mailosaur* as a test email. please create a account of mailosaur)
		
4. Pre-action
	1. Check if the driver is the latest version
	```sh
	# Install chromedriver latest
	sbase install chromedriver latest 
	# chromedriver for Chrome, edgedriver for Edge, geckodriver for Firefox
	```

5. Run tests
	1. Run your tests:
	```sh
	python3 -m pytest tests/test_login.py --html=report/report.html
	``` 
	2. Run your tests with locales:
	```sh 
	python3 -m pytest tests/test_login.py --locale=[zh-tw|en-us]
	```
	3. Run your tests by browser:
	```sh
	python3 -m pytest tests/test_login.py --browser=[chrome|firefox|safari]
	# Run safaridriver --enable once in a terminal to enable Safari's WebDriver. (If you’re upgrading from a previous macOS release, you may need to prefix the command with sudo.)
	```
	4. Run your tests on the Selenium Grid:
	```sh
	python3 -m pytest tests/test_login.py --server=IP_ADDRESS --port=4444. 
	```


## troubleshooting
1. Q : This version of ChromeDriver only supports Chrome version 77
```sh
# Install chromedriver latest
sbase install chromedriver latest 
```