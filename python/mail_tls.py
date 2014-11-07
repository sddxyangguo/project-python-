#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import getopt
import sys

class main(object):
    def __init__(self,opts):
        self.sender = 'dingning@ucloudworld.com'
        self.username = 'dingning@ucloudworld.com'
        self.password = 'lejuA8768'

        
        self.receiver = opts['-t']
        self.subject = opts['-s'] 
        self.message = opts['-m']
    def __call__(self):
        
        msg = MIMEText(self.message,'plain','utf-8')
        msg['Subject'] = Header(self.subject, 'utf-8')
        msg["From"] = self.sender
        msg["To"] = str(self.receiver)
        msg["Reply-To"] = self.sender


        smtpserver = 'smtp.partner.outlook.cn'
        server_port = 587

        smtp = smtplib.SMTP(smtpserver,server_port)
        smtp.set_debuglevel(1)

        smtp.ehlo()
        smtp.starttls()
        smtp.login(self.username, self.password)

        smtp.sendmail(self.sender, self.receiver, msg.as_string())
        smtp.quit()


def get_command_options(args):
    """
        run 
        -t    mailadder
        -m    messsage
        -s    subject
        -h    usage
         
    """
    getoptions = getopt.gnu_getopt
    try:
        options = getoptions(args, "t:m:s:h")
    
    except Exception as msg:
        raise Exception, "get options error. %s" % msg
    return dict(options[0])



if __name__ == "__main__":

    opts = get_command_options(sys.argv[1:])    
    if opts.has_key("-h"):
        sys.exit(get_command_options.__doc__)     
               
    print opts

    m = main(opts)
    m()
#     m()