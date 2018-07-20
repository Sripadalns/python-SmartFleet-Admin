# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# Define these once; use them twice!
strFrom = 'info@intracworks.com'
strTo = 'sripadalns@gmail.com'
string = 'SriChaitanya'
# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'School Bus Managment Exclusively for  ' + string + '!!!!!'
msgRoot['From'] = 'Team InTracWorks'
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('Get School Bus Tracking @ 333 / month onwards.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<b>InTracWorks offer school bus managment system  <i>@ Rs 333 / Month exclusively for you HTML</i> text</b> <img src="cid:image1"><br>', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('Intro.PNG', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)
import smtplib

username = 'info@intracworks.com'
password = 'awesomesupport@ITW'


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(strFrom, strTo, msgRoot.as_string())
server.quit()
