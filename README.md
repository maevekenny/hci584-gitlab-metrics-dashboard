# GitLab Metrics Dashboard

This app will be used to show significant metrics on how a team is performing during their software release schedule. GitLab is a web application that is used as a software development lifecycle and version control tool. It allows software teams to store code, write documentation and track issues in a continuous integration environment. This application is written in Python utilizing Flask as the web framework and PyCharts for data visualization.

## Requirements

- [Python](https://www.python.org/) - Main language that comes with package installer
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
- [NPM](https://www.npmjs.com/) - Node package installer
- [Git](https://git-scm.com/) - Dependency Management
- [BootStrap](https://getbootstrap.com/) - Dark dashboard framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Flexible SQL database

## Installation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

To see more architecture, high-level details of the system, bugs, and future enhancements, refer to the [Developer Guide](./docs/developer-guide.md).

### Get Code

To get the code, enter the following command into your terminal:

```bash
git clone https://github.com/maevekenny/hci584-gitlab-metrics-dashboard.git
```

### Requirements

To install the external Python package requirements, enter the following command into your terminal:

```bash
pip install requirements.txt
```

To install the external node modules, enter the following command into your terminal:

```
npm install
```

## Running the application

To run the application locally, enter the following command into your terminal:

```bash
python main.py
```

Navigate to http://127.0.0.1:5000/ in your browser to access the project.

**!!NOTE!! -** For ease of development, there is a GitLab username and token stored in the project so a tester doesn't have to create a new account.

## Author

- **Maeve Kenny** - maevek@iastate.edu
