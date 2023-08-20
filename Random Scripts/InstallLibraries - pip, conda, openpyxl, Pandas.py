"""
Created June 2023 by Tanner Hammond
Python ver. 3.9.16
This code is partially untested
"""

#Install pip and Conda
import subprocess
import sys

def install_pip():
    try:
        # Check if pip is already installed
        subprocess.check_output([sys.executable, '-m', 'pip', '--version'])

        # Print a message if pip is already installed
        print("pip is already installed.")

    except subprocess.CalledProcessError:
        try:
            # Run the command to install pip
            subprocess.check_call([sys.executable, '-m', 'ensurepip', '--default-pip'])

            # Print a success message
            print("pip installed successfully.")

        except subprocess.CalledProcessError as e:
            # Print an error message if the installation fails
            print("pip installation failed: ", e)

def install_conda():
    try:
        # Run the command to install conda
        subprocess.check_call(['pip', 'install', 'conda'])

        # Print a success message
        print("conda installed successfully.")

    except subprocess.CalledProcessError as e:
        # Print an error message if the installation fails
        print("conda installation failed: ", e)

#Install pip if it's not already installed
install_pip()

#Call the function to install conda
install_conda()

#Install openpyxl
import subprocess

def install_openpyxl():
    subprocess.check_call(['pip', 'install', 'openpyxl'])

install_openpyxl()

#Install Pandas
import subprocess

subprocess.check_call(['pip', 'install', 'pandas'])

