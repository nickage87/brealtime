from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webservice():
    if request.method == 'POST':
        data_received = request.headers
        print data_received
    else:
	if request.args.get("q") == "Ping": 
            return 'OK'
	elif request.args.get("q") == "Name":
            return 'Nikolay S'
        elif request.args.get("q") == "Status":
            return 'Yes, I can'
        elif request.args.get("q") == "Referrer":
            return 'Recruiter: Darren C.'
        elif request.args.get("q") == "Resume":
            return "http://here/resume.docx"
        elif request.args.get("q") == "Source":
            return "https://github.com/nickage87/brealtime.git"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
