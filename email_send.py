# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
def send_email( Toaddr,SchoolName ):
    # Define these once; use them twice!
    strFrom = 'info@intracworks.com'
    strTo = Toaddr 
    string = SchoolName
    string1 = ' Only For '
    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'School Bus Managment Exclusively for  ' + string + '!!!!!'
    msgRoot['From'] = 'Team InTracWorks'
    msgRoot['To'] = strTo

    #We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('<b> <font size="4"><font face="Century Gothic" ><font color="#487F81">'+ '@ Rs 333 / Month  onwards'+ string1+ string+' </font></font></font></b>' +'<img src="cid:image1"><br>', 'html')
    msgRoot.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open('Intro.PNG', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgImage.add_header('Content-Disposition','inline',filename='SmartFleet.png')
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

