## What is boto3?
boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python. It allows Python developers to write software that makes use of services like Amazon S3, EC2, DynamoDB, and more. boto3 makes it easy to integrate your Python application, library, or script with AWS services. It provides an object-oriented API as well as low-level access to AWS services.

## How to Download a File from AWS S3 using Python
This tutorial will guide you through the process of downloading a file from an AWS S3 bucket using Python. 
Prerequisites
Ask for Access key ID and Secret access key from UW-Madison Research drive team, set them as environmental variables for security.
### On macOS (or Linux)
1.	Open Terminal.
2.	Edit your shell profile file. This file could be one of several, depending on your shell. Common files include ~/.bash_profile, ~/.bashrc, ~/.zshrc, etc. If you're using Bash, you'll likely edit ~/.bash_profile or ~/.bashrc. If you're using Zsh (the default on newer versions of macOS), you'll edit ~/.zshrc.
3.	Add your S3 credentials to the file. Open the file in a text editor (you can use nano or vim directly from the terminal). Then, add the following lines at the end of the file:
   
```
export S3_ACCESS_KEY_ID='your_access_key_id_here'
export S3_SECRET_ACCESS_KEY='your_secret_access_key_here'
Replace your_access_key_id_here and your_secret_access_key_here with your actual AWS access key ID and secret access key.
```
4.	Save and close the file. If you're using nano, you can do this by pressing Ctrl + O, Enter, and then Ctrl + X. In vim, you can do this by typing :wq and then pressing Enter.

5.	Reload the profile. To make the changes effective, you can either close and reopen your terminal or source the profile file with a command like source ~/.bash_profile or source ~/.zshrc, depending on which file you edited.

### On Windows
1.	Open System Properties. Right-click on the Start button, select System, then click on Advanced system settings on the left sidebar.
2.	Environment Variables. In the System Properties window, go to the Advanced tab and click on the Environment Variables button near the bottom.
3.	Add new user variables. In the Environment Variables window, under the User variables section, click New to create a new variable. Create two variables:
```
Variable name: S3_ACCESS_KEY_ID
Variable value: your_access_key_id_here
Variable name: S3_SECRET_ACCESS_KEY
Variable value: your_secret_access_key_here
Replace your_access_key_id_here and your_secret_access_key_here with your actual credentials.
```
4.	OK and Apply. After adding both variables, click OK on all open dialog boxes to apply these changes.
5.	Restart any open command prompts or applications. To ensure these environment variables are recognized, you may need to restart any command prompts, PowerShell windows, or applications where you intend to use these credentials.
By setting these environment variables, you avoid hardcoding your credentials in your scripts, enhancing security. 

### More functions check the .py file for detail
