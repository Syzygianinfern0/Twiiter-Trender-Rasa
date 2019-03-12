# Lazy Rasa Scripts

This is a collection of all scripts or shortcuts I may be using for Rasa training and running automation

Clone it with 
```bash
git clone https://github.com/Syzygianinfern0/Rasa-Scripts.git
```
 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Rasa.

NLU
```bash
pip install rasa_nlu
```
CORE
```bash
pip install rasa_core
```
Use Tensorflow for the pipeline.  For intent classification & entity extraction

```bash
pip install rasa_nlu[tensorflow]
```
## Usage

### Training the NLU model
 To train and test the model run:  

``` python nlu_model.py ```

### Training the Rasa Core model

Custom actions to be run on actions.py and deployed on a server. That server has to be configured in a 'endpoints.yml' file.  This is how to train and run the dialogue management model:  
1. Start the custom action server by running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. Open a new terminal and train the Rasa Core model by running:  

``` python dialogue_management_model.py```  
 
3. Talk to the chatbot once it's loaded.  

### Starting the interactive training session:

The process of running the interactive session is very similar to training the Rasa Core model:
1. Make sure the custom actions server is running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. The interactive session also creates a graph.html. Be sure to check that out. Start the interactive training session by running:  

``` python train_interactive.py ```  
   
## Deploy on Messenger
### Managing Credentials

How to get the FB credentials: You need to set up a Facebook app and a page.

1. To create the app head over to Facebook for Developers and click on My Apps -> Add New App.
2. Go onto the dashboard for the app and under Products, find the Messenger section and click Set Up. Scroll down to Token Generation and click on the link to create a new page for your app.
3. Create your page and select it in the dropdown menu for the Token Generation. The shown Page Access Token is the page-access-token needed later on.
4. Locate the App Secret in the app dashboard under Settings -> Basic. This will be your secret.
5. Edit the run_app.py file to match the credentials you have got. Have a verify token as a string of your choice.
6. Set up a Webhook on messenger and select at least the messaging and messaging_postback subscriptions. 

### The Actual Part
1. If you’re testing on your local machine (e.g. not a server), you will need to use [ngrok](https://ngrok.com/). This gives your machine a domain name and so that facebook, slack, etc. know where to send messages.
2. Start off Custom Actions from you actions.py file
```bash
python -m rasa_core_sdk.endpoint --actions actions
```
3. Start your agent with the
```bash
python run_app.py
```
4. Start your ngrok on port 5004 (or as configured in run_app.py)
```bash 
ngrok http 5004
```
5. Insert your callback URL on webhook of your app in Edit Subscription page of which will look like https://<YOUR_HOST>/webhooks/facebook/webhook. YOUR HOST will be the forwarding URL as obtained from ngrok forwarding (eg : https://6010db3b.ngrok.io ) . Insert the Verify Token which has to match the verify entry in your run_app.py.

6. Talk with your bot on [facebook messenger](https://www.messenger.com) refering to the username of the page you created.
   
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

