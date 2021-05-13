# My_Learning_WhatsApp
Learn how to create a WhatsApp Bot

## About
* Facebook has allowed business companies like Twilio to provide the WhatsApp API.

## Installation
### Packages
1. twilio - `pip install twilio`
1. flask - `pip install flask`
1. ngrok - `pip install pyngrok` (for communication b/w the code & whatsapp in testing purpose)

### Configuration
1. Sign up with Twilio [here](https://www.twilio.com/)
1. Setup the "Twilio Sandbox for WhatsApp" [here](https://www.twilio.com/console/sms/whatsapp/learn) which lets you test your app in a developer environment."
1. Opt-in to the Sandbox: Send a message now to like [this](https://www.twilio.com/docs/whatsapp/quickstart/python#sandbox-opt-in-message) to https://api.whatsapp.com/send/?phone=%******* shown in this [url](https://www.twilio.com/console/sms/whatsapp/learn), after saving this no. as "KYC Bot" for example.
1. After success, this is shown:
```md
Congrats. Your WhatsApp phone number is now linked to your Sandbox.
Next, let's send a One-Way WhatsApp Message from your Sandbox.
```

## Getting Started
1. Write the code like [this](./tutorials-py/tut_1.py)
1. Open CMD in this directory, then run `> python tut_1.py`
```console
>python tut_1.py
 * Serving Flask app "tut_1" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
1. So, now in order to connect your whatsapp with the code, 
	- type `> ngrok` in CMD & it will install after `pip install pyngrok`
	- `> ngrok http 5000`
```console
ngrok by @inconshreveable                                                                               (Ctrl+C to quit)                                                                                                                        Session Status                online                                                                                    Session Expires               1 hour, 48 minutes                                                                        Version                       2.3.40                                                                                    Region                        United States (us)                                                                        Web Interface                 http://127.0.0.1:4040                                                                     Forwarding                    http://dc315ad60c1e.ngrok.io -> http://localhost:5000                                     Forwarding                    https://dc315ad60c1e.ngrok.io -> http://localhost:5000                                                                                                                                                            Connections                   ttl     opn     rt1     rt5     p50     p90                                                                             0       0       0.00    0.00    0.00    0.00
```
1. Copy ngrok forwarding url `http://dc315ad60c1e.ngrok.io` & paste into the param - "WHEN A MESSAGE COMES IN" [here](https://www.twilio.com/console/sms/whatsapp/sandbox)
1. Now, during usage, it shows like this:
```console
[1:38 AM, 5/13/2021] Abhijit Roy: how are you
[1:38 AM, 5/13/2021] Twilio WhatsApp: You said :how are you.
 Configure your WhatsApp Sandbox's Inbound URL to change this message.
```
1. So, the problem is the URL in WhatsApp Sandbox has to be changed with this:

## Keywords
* TwiML - Twilio Markup Language | the response format alternative format of JSON

## References
* [Console: Get the SSID, Auth token from here](https://www.twilio.com/console)
* [Get started with the Twilio Sandbox for WhatsApp](https://www.twilio.com/docs/whatsapp/sandbox)
* [Webhook](https://www.twilio.com/docs/glossary/what-is-a-webhook)
* [Mridu Bhatnagar: Building a Conversational Bot for WhatsApp w/Twilio & Python](https://www.youtube.com/watch?v=dqab-FcAirA)