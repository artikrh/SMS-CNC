# SMS C&C with Python and Twilio

## 1. Overview

The objective of this project is to build and implement a SMS bot using Python and the Twilio API (Application Programmable Interface). This will allow arbitrary function implementations that will be invoked by a simple text message over the 2G GSM (Global System for Mobile) network - without the need of even using 3G/LTE connections.

## 2. System Architecture

The system is comprised of three parts:
1. Flask for Python - the micro web framework which runs the application locally
2. Twilio REST API - cloud based service that enables communication between devices and our application
3. Ngork - establishes secure tunnels from a public endpoint such as internet to our local service


## 3. Installation

Initially, you are going to need Python installed on your system. The Flask application uses Python 2.7:  
```
$ python --version  
Python 2.7.X
```
Since we are going to use the Twilio API and Flask, we are going to install the python libraries using PIP as a packet manager:
```
$ git clone https://github.com/artikrh/SMS-CCC
$ sudo pip install -r requirements.txt
```
Run the Flask application:
```
$ chmod +x run.py
$ ./run.py
```
In another terminal window, we also need to download the `ngork` binary from their website:
```
$ wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
$ unzip ngrok-stable-linux-amd64.zip
```
An authentication token is required from https://dashboard.ngrok.com/auth to use the service:  
`$ ./ngrok authtoken <YOUR_AUTH_TOKEN>`

Start the HTTP tunnel on port 5000 (where Flask is going to be running at):  
`$ ./ngrok http 5000`

Next, we are going to set up Twilio by registering an account to their service and add an active phone number which has SMS capabilities (cost-free). We also set up a messaging service as a two-way interactive chat in which we add our *.ngork.io URL to inbound settings to process HTTP POST requests. This is the connecting point between the API and our system which uses the API to perform arbitrary actions.

## 4. Usage

After you have set up a Twilio phone number, you only need to write further Python code to implement your own functions. You will find a sample included in `run.py`:  

```
    if "killbill2" in message:
        answer = "Killed Bill 2"
```
This means that if the string `killbill2` is detected in the inbound SMS message from our phone number (which we registered Twilio account with), it is going to reply an answer of "Killed Bill 2".  

Furthermore, there is another function defined called `removeHead()` which could allow you to perform the following scenario as an example:  
* Receive a SMS `message` with the content of: "cmd ls -lah"
* cmd = removeHead(message,"cmd") # means that `cmd = "ls -lah"`
* `answer` is the output of `cmd` execution  
* Reply SMS  
