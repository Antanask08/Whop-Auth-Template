import hashlib
import platform
import requests
import os
import sys

# Vars Needed for auth

apikey = "" # api key from whop dashboard
prodid = "" # product id from whop dashboard

# Check for config file


if os.path.isfile("config.txt") == True:
    file = open("config.txt", "r")
    config = file.readline(0)
    file.close
    config.split(",")
    if len(config) == 0:
        print("config file empty")
        
else:
    whopkeys = str(input("Enter Your Whop Key"))
    # Add any other inputs you want to add to the file 
    
    file = open("config.txt", "w")
    config_text = str(whopkeys) # add any other things
    file.write(config_text)
    file.close()
    print("Bot restart needed")
    input("Press enter to close the bot")
    sys.exit()




whopkey = config.__getitem__(0) # grabs first thing infront of the ,




def validate_license(whopkey, prodid):

   
    HWID = hashlib.sha256(platform.node().encode()).hexdigest().strip()



    url = f"https://api.whop.com/api/v2/memberships/{whopkey}/validate_license"

    payload = {"metadata": {"HWID": HWID}}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {apikey}",
        "content-type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    
    data = response.json()
    valid_response = data["valid"]
    product = data["product"]    
    response_code = response.status_code
    product_check = product == prodid
    if product_check == False:
        print("This key is not for the doordash chain bot, if this is an error contact admin asap!")  
        input("Press any key to exit!")
        sys.exit()  
    
    if valid_response == True:
        print("License is valid!")
    else:
        print("Invalid License")
        input("Press any key to exit")
        sys.exit()
    
validate_license(whopkey, prodid) # calls the function
    
    
