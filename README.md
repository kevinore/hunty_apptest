# Hunty Test APP 💜🚀 



##### Python 3.9 or later supported
##### Service Host: https://api.app-test.link/api/v1/
##### Api Documentation: https://api.app-test.link/api/v1/docs
##### Postman Collection: https://www.getpostman.com/collections/54a36ced693add50915f

The project use these resources: 

1. AWS EC2 Instance
2. Cloudflare DNS Service
3. SSL certificate and my own domain 
4. Docker Container inside AWS instance (Hunty test app and Nginx)
5. MongoDB Cluster instance


### Run locally

1. Create and activate your environment remember use python 3.9 or later
    ```
    virtualenv -p python3.9 venv
    ```
2. Activate the environment
    ```
    source venv/bin/activate
    ```
3. Install requirements.txt
    ```
    pip install -r requirements.txt
    ```
4. Set up the .env file based on the .env.example
5. Run the project
    ```
    python app_main.py
    ```
   now go to **http://0.0.0.0:5000/api/v1/** and check if everything is okay

### Run unit tests locally

1. Go to `test` directory and run
    ```
    pytest
    ```
   This will run the tests and show the result in the console

