from flask import Flask, request, jsonify
import socket
import subprocess

app = Flask(__name__)

@app.get('/')
def handle_get():
	hostname = socket.gethostname()
	address = socket.gethostbyname(hostname)
	return str(address)

@app.post('/')
def handle_post():
	p = subprocess.Popen(["python3", "stress_cpu.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	return '200'
