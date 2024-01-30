# Laurkan - Medial Health Take Home Project Supplemental

This is a test server for that performs persistence independent of the client. 
The client only knows urls and that communication is performed in JSON. 
No encryption is being performed at this time.

Additionally, this provides a manual way to add assignees via the /add_assignee page.

## Installing
Clone the repo and open a terminal in the folder with the Pipfile. Assuming you have Python and the pipenv packager on your machine, run the following commands:
```pipenv shell```
```pipenv install```
This should get all the Flask dependencies installed on a virtual environment, as well as start that environment for you in the terminal. 

## Running the Server
Once you are in the pipenv virtual environment, you can run.
```python app.py```
This command will start a server on localhost at port 5001 by default. If you do not want that port, feel free to edit the app.run(<port>) command in the main method of app.py. Just be aware you will have to also change some variables in the React App as well, as the assumption is port 5001 is available.

