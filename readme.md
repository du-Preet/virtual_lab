# VirtualLabX

VirtualLabX is a hardware simulator.

## Description

VirtualLabX is a hardware simulator.

## Getting Started

### Dependencies

* Windows 10
* Python 3
* Check requirements.txt for PIP packages

### Installing

* Download and Install the latest Python
* Clone / Download the project files in to your local windows machine
* Once downloaded go to the project directory i.e. vlab directory
* Open a terminal / powershell in the same directory
* Create a virtual environment using command "py -m venv env" (This will create a env folder in the current directory)
* Then activate the environment using command ".\env\Scripts\activate" (If you get error check Troubleshooting)
* Then install the dependencies using command "pip install -r requirements.txt"
* The above step will download all the packages over internet. Make sure your system has internet access.

### Executing program

* Run the application using command "python3 app.py"

## Authors

Contributors names and contact info

Preet
Email geekypreet1989@gmail.com

## Version History

* 0.0
    * Basic project
* 0.1
    * Initial Release

## Acknowledgments


** Troubleshooting

* For error "PowerShell says "execution of scripts is disabled on this system.""
* Enter below command in the terminal / powershell:
* "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"
