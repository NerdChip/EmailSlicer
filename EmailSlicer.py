#Email Slicer
#author Gamuchirayi MAnungo
#The email slicer is a handy program to get the username and domain name from an email address. 
#You can customize and send a message to the user with this information.

#Imported Libraries
import pyinputplus as pyip



print("Welcome to the Email Slicer Program, Enter an Email addresses, We will slice it and give you the username and domain\n")
print("Please follow instuctions as you go along the program\n")


#prompt user for input, using pyinputplus to validate user input
response = pyip.inputEmail(prompt='[*]Please Enter an Email addresse<>  ',limit=3,default='Limit has been met!')

#Function that slices the user input into two, uterlising the split function.
def slice(x):
	print("[*]slicing the address...")
	username = x.split('@')[0]
	domain_name = x.split('@')[1]
	print("[*]slice complete...")
	return username, domain_name

#retriving the result from the function it will be passed back as a tuple, and calling the function to execute as well. 
result = slice(response)

#accessing the vaules returned in the tuple and assinging the to a variable
name = result[0]
domain = result[1].split(".")[0]

#output passed back to the user telling them the user name and domain of the email they have provided
print(f"[*]The username of this email addresses is {name}, The domain is {domain}.")
print("[*]Thanks\n")
# request if user wants to send email to the email provided 
print("[*]would you like to send this person an email, Please Select yes or no.")
#using pyinputplus to validate user input 
response_2 = pyip.inputYesNo(prompt='[*] Yes or No <> ')


#main funtion to send email to the user
def mailuser(x):
	#imported libs
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	#request from user what they want said in the body of the email.
	mail_body = input("[*]Please input what the you want to say in the email below>\n")

	#Request the users sender Addresses and password, again using pyinputplus to validate user input 
	sender_addresses = pyip.inputEmail(prompt='[*]Please Enter Your Gmail Account Email addresse> ',limit=3,default='Limit has been met!')
	password = pyip.inputPassword(prompt='[*]Please Enter Your Gmail Account password> ',limit=5)
	
	#defining header that are to be passed with the email.
	message = MIMEMultipart()
	message['From'] = sender_addresses
	message['To'] = x
	message['Subject'] = pyip.inputStr(prompt="[*]Please Enter Email subject  \n")

	message.attach(MIMEText(mail_body,'plain'))
	try:
		session = smtplib.SMTP('smtp.gmail.com', 587) # connecting to google SMTP server
		session.starttls() # initiating tls encryption 
		session.login(sender_addresses,password) #logging into SMTP server 
		text = message.as_string()
		session.sendmail(sender_addresses,x,text)# send email from your address to chossen address along with the text
		session.quit()#close session
		print('mail sent')
	except smtplib.SMTPException:# error handerling 
		print("[-]Error: unable to send email please check inputed parameters")

#request if user wants to send email to choosen email if so call the mailuser function passing the email as a parameter.
if  response_2 == 'yes':
	mailuser(response)
else:
	print("Thank you for using the email slicer goodbye")
	









