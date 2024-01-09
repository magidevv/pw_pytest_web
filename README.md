# Description

Basic playwright + pytest testing framework. Framework displays how to test different Ul elements and scenarios utilising https://demoqa.com/ as a testing sandbox.
Framework utilises functionality of the Allure reporter. Reports are stored and displayed via GitHub Pages. Also, there is an integrated Slack notification when GitHub Actions runs.

## Repository Structure

The repository includes the following key directories and files:

- `.github`: Configuration files for GitHub actions.
- `data`: Directory containing test data.
- `utils`: Directory containing useful functions and modules.
- `tests`: Directory for organizing test files.
- `pages`: Test page objects.
- `.env`: Environment variables configuration file.
- `.gitignore`: File specifying which files and directories to ignore in version control.
- `pytest.ini`: Project's package file containing a number of configuration values that are applied to all test runs for project.
- `conftest.py`: Configuration file with custom fixtures.

## Installation

To install and set up this project from the GitHub repository, follow these steps:

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/magidevv/pw_pytest_web.git
   ```

2. Change to the project directory:
   ```shell
   cd your-repo
   ```

3. Install environment:
   ```shell
   python -m pip install --upgrade pip
   pip install pipenv
   pipenv install --system
   playwright install
   ```

4. Install dependencies:
   ```shell
   pipenv install python-dotenv
   pipenv install faker
   pipenv install pytest-xdist
   ```

## Run Playwrigth tests

- Run all set of tests:
  ```shell
  pytest
  ```

- Run one particular test:
  ```shell
  pytest -k <name of the test>
  ```

- Run tests marked with a specific mark:
  ```shell
  pytest -m <name of pytest mark>
  ```

- Run tests on different browsers:
  ```shell
  pytest --browser <name of browser>
  ```

- Run tests in parallel:
  ```shell
  pytest --numprocesses <number of processes>
  ```

## Generate Allure report

Test report is generated automatically after each test run overriding the previous report.

- To open the report in your default web browser, run:
  ```shell
  allure serve reports
  ```