# Bot-U
Create chatbot out of your Facebook chat logs.

  - Download your Facebook chat logs
  - Put them into Bot-u
  - Enjoy immortal copy of yourself

Bot-u is written in the Python3 with usage of scikit-learn's TF-IDF.

### Requirements
  - Python3
    - If you use Windows and you have problem with SciPy, then I recommend Anaconda which contains SciPy
  - scikit_learn
    - scikit_learn itself requires NumPy and SciPy

##### Warning!
**Do not share your bot with anybody unless you are 100% sure that your chat logs don't contain any sensitive informations. Chatbot will use lines from your logs as answers, so it can answer with something which you don't want to share publicly. Clean your chat logs, if you want to share your chatbot. I don't have any responsibilities for problems caused by not following this advice.**

## USAGE
### Facebook chat logs download
Facebook allows you to download your whole history of activities. We are interested in the chat logs. Following steps explains you how to get them.

#### 1) Go to settings
Log into your Facebook account and go to ``Settings``.
![Settings](https://raw.githubusercontent.com/ermrk/Bot-u/images/bot-u-1.png)

#### 2) Get a copy of your Facebook data
Go to ``General`` and click on ``Download a copy`` down on the page.
![Download a copy](https://raw.githubusercontent.com/ermrk/Bot-u/images/bot-u-2.png)

#### 3) Start the archivation
Click on the ``Start My Archive`` button. Confirm your action. Link to your archive will be send to your email.
![Start archivation](https://raw.githubusercontent.com/ermrk/Bot-u/images/bot-u-3.png)

#### 4) Get link to archive from your email
You will receive email with link to your archive after a while. Click on the link in the email.
![Email link](https://raw.githubusercontent.com/ermrk/Bot-u/images/bot-u-4.png)

#### 5) Download archive
Download your archive by clicking on ``Download Archive`` button.
![Download archive](https://raw.githubusercontent.com/ermrk/Bot-u/images/bot-u-5.png)

#### 6) Get chat logs
Open the downloaded archive. We are interested in the file ``html\messages.htm``. Copy it somewhere, we will need it later.
![Logs file](https://raw.githubusercontent.com/ermrk/Bot-u/images/bot-u-6.png)

##### Friendly remainder
**You will download files containing your personal informations. Do not share them with anybody!**

### Running Bot-U
Copy file ``messages.htm`` into folder of Bot-u (that containing file ``main.py``). 

Install requirements by:
```sh
$ pip install -r requirements.txt
```

Run the Bot-u by:
```sh
$ py -3 main.py "John Smith"
```
Put your Facebook name instead of ``John Smith``. Name is used to parse messages from ``messages.htm`` file correctly. Bot-u will create file data.json containing parsed messages (you can use this file as dataset for your own chatbot running on different technology). You can start chatting with yourself right after message ``"I am ready! Let's chat."``.

**Pull requests adding connection to Facebook messenger are welcomed!**