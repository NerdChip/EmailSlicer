# EmailSlicer
Project 3 of my python journey, I have created an email slicer. Program the requests the user to input an email address, it provides the user with the username and
domain name of the email. When slicing is complete the user can send an email to the user from their google account using google SMTP server. This is all done in the 
terminal.

# Requirements 
- python 3.6 and above
- Turn Allow less secure apps to ON. Be aware that this makes it easier for others to gain access to your account.(https://myaccount.google.com/lesssecureapps)

# Dependencies 
-pip install pyinputplus - user input validation 
-pip install smtplib (Thia package should be already available when python is downloaded)
-email.mime.multipart 
-email.mime.text


# Guide - How to Use 
python EmailSlicer.py

# Support 
Please if you have and ideas on how this can be improved feel free to suggest changes. Additionally if you find and bug please report them. 

# Improvements
*In the future i am looking to add a domain reputation look up to help identify if the email has come from an untrusted source with the possibility of is being phishing emial or not.
