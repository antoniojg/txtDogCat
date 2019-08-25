from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import random

# removed private twilio client information
client = Client("XXXXXXXXX", "XXXXXXXX")


def sendImage(num, msg):

    # List with dog image links
    imagesLinkDog = ('https://images.unsplash.com/photo-1455103493930-a116f655b6c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1351&q=80',
                  'https://images.unsplash.com/photo-1535479572772-4b963399c626?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80',
                  'https://images.unsplash.com/photo-1566395712004-df883ede22d3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=625&q=80',
                  'https://images.unsplash.com/photo-1560293918-bd3b0f367889?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1387&q=80',
                    'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80',
                   'https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80',
                   'https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=660&q=80')

    #List with cat image links
    imagesLinkCat = ('https://images.unsplash.com/photo-1543852786-1cf6624b9987?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80',
                   'https://images.unsplash.com/photo-1488740304459-45c4277e7daf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80',
                     'https://images.unsplash.com/photo-1455970022149-a8f26b6902dd?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2148&q=80',
                     'https://images.unsplash.com/photo-1529933037705-0d537317ae7b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=671&q=80')

    #If the user text anything either than 'dog' or 'cat', send this image
    errorImg = 'https://images.unsplash.com/photo-1455380579765-810023662ea2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80'

    #Flow to determine which list to grab an image from, or error
    if msg.lower() == "cat":
        media = random.choice(imagesLinkCat)
        response = "Here is your cat!"
    elif msg.lower() == "dog":
        media = random.choice(imagesLinkDog)
        response = "Here is your dog!"
    else:
        media = errorImg
        response = "Sorry, please text us back with either 'cat' or 'dog'."

    # Handle the number, message, and response
    number = "+" + num
    message = client.messages \
              .create(
                  body=response,
                  from_="+18722313670",
                  media_url=[media],
                  #to="+17088340214"
                  to=number
                )

    print(message.sid)

# Creating the Flask App
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def smsReply():
    
    from_number = request.form['From']
    to_number = request.form['To']
    body = request.form['Body']
    
    resp = MessagingResponse()
    resp.message(sendImage(from_number, body))
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
