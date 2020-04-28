# VCheck 

VCheck is a python module to scrap data from Gunadarma's V-Class Website without hassle.

## Installation

Install `virtualenv`:

```bash
pip install virtualenv
```

Create new `virtualenv` and install depedencies:

- Windows:

    ```
    virtualenv venv
    venv\Scripts\activate &&
    pip install -r requirements.txt
    ```

- Linux / MacOS:

    ```bash
    virtualenv venv &&
    . venv/bin/activate && 
    pip install -r requirements.txt
    ```

Install `geckodriver`

- Windows:

  - Download latest `geckodriver.exe` from [here](https://github.com/mozilla/geckodriver/releases/).
  - Unzip and move / copy `geckodriver.exe` into your `venv\Scripts\` folder.

- Linux / MacOS:

  - Download latest `geckodriver` from [here](https://github.com/mozilla/geckodriver/releases/).
  - Untar and move / copy `geckodriver` into your `/usr/bin` or any other directory inside `PATH`.

## Usage

Always use `virtualenv` when interacting with these modules

- Windows:

  ```
  venv\Scripts\activate
  ```

- Linux / MacOS:

  ```bash
  . venv/bin/activate
  ```

### Run on terminal

```bash
python vcheck.py
```

### Import as module

```python
from vcheck import VCheck

driver = VCheck() # Create new instance of VCheck

# Login as username with correct password
driver.login(username, password)

# Check login status
driver.auth # returns True / False

# Get a list of upcoming tasks
upcomingTasks = driver.getUpcomingTask()

# Get a list of current enroled course
courseList = driver.getCourseList()

# Terminate connection with VClass site
driver.endConnection()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU GPLv3.0](https://github.com/Rayhanga/VCheck/blob/master/LICENSE)