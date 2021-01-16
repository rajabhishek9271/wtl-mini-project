from django.core.mail import send_mail
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

def sendMailToUser(name, send_to):
    subject = "Thanks for contacting us"
    message = "Hello "+name+"! \n\nWe have successfully received your message.\n\nWe will get back to you as soon as possible."
    try:
        send_mail(
            subject,
            query,
            env("EMAIL"),
            [send_to],
            fail_silently = False,
        )
    except:
        print("Email Not Sent")


def sendMailToCharity(name, email, query):
    message = "A new message has been received on our website:\n\nName: "+name+"\nEmail Id: "+email+"\nMessage: "+query+"\n\n\nRegards"
    subject = "A message has been received."
    send_mail(
        subject,
        query,
        env("EMAIL"),
        ['abhishekraj1729@gmail.com'],
        fail_silently = False,

    )