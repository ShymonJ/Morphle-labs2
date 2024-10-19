from flask import Flask
import time
import subprocess


app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Shymon Jagath"
    
    username = subprocess.getoutput("whoami")
    
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    top_output = subprocess.getoutput("top -bn1")
    
    return f"""
    <h2>Name: {full_name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '_main_':
   
    app.run(host='0.0.0.0', port=5000)