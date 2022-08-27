# fastapi-crud-jwt-postgresql
The repository shows how to use FastAPI CRUD (Create, Read, Update, Delete) operation, securing endpoints using jwt bearer tokens and postgresql to save the data.

To run the project follow below steps

Step 1:

Create System Evnironment Variables

codeblog_username = "set your postgresql username"<br />
codeblog_password = "set your postgresql password"<br />
codeblog_hostname = "set your hostname -> localhost or 127.0.0.1"<br />
codeblog_database = "set the name of password"<br />
codeblog_secret_key = "your secret key"<br />

On Windows

Window -> Edit the system environment variable -> Environment Variables -> System Variables -> New -> Set all variables with their values

On Linux (ubuntu 22.04)

vi .bashrc or nano .bashrc
export variablename="variable value"

NOTE: There should be no space between variableName=variableValue


