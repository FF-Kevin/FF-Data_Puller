# Data Puller
## _Tool used to pull all data from analyzers_
_Note: Currently only works on the Nova Analyzer_

#### Getting started: Installing Python
---
This tool requires the use of python, make sure to download the latest release of [Python](https://www.python.org) to make sure this works. When installing python make sure you also install pip

#### Getting Started: Installing addition packages needed
---
Before using the python script to make concat all you data make sure you install all the prereqs needed if this is your first time. Run the following command:

`pip install -r requirements.txt`

Make sure the `requirements.txt` file is from the one provided in this repository. You might have to add in the file path if it does not initially work

#### Running the Tool
---
Using a command prompt run the following command and lauch Jypyter Lab:

`jupyter lab`

If correctly executed, your default browser should automatically pop up and you should be able to navigate to folder that contains the tool

From here make sure you open the file `data_puller.ipynb` by double clicking on it

Finally run the cell that contains the code and an interface should pop up underneath. You can interact with this interface. Follow the instructions on the top of the notebook for assistance.


#### Troubleshooting
---
__Issue 1: pip not found__
- If pip is not found make sure you enable the install of pip when installing python. There should be a checkbox prompting to you install pip.
- Also make sure to enable the use of PATH to allow you to run the commands on a command prompt 

__Issue 2: Error locating files__
- If issues arises where you can't fine a file try running it as a file path instead of just file name, for example:
`pip install -r "your/file/path/here/requirements.txt"`
- This might also apply when trying to run the python tool where `main.py` will need to be the file path
- You can also just change your working directory to the file where the tool is located using:
`cd your/file/path/here`