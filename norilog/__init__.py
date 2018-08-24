from flask import Flask

application = Flask(__name__)

def main():
	application.run("127.0.0.1", 5000)
	
if __name__ == "__main__":
	application.tun("127.0.0.1", 5000, debug=True)

