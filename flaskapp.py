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
        elif request.args.get("q") == "Position":
            return 'Sr. Devops Engineer'
        elif request.args.get("q") == "Resume":
            return "http://52.15.70.14/files/resume.docx"
        elif request.args.get("q") == "Source":
            return "https://github.com/nickage87/brealtime.git"
        elif request.args.get("q") == "Puzzle":
            return "not solved yet source " + request.args.get("d")
        elif request.args.get("q") == "Years":
            return "I have experience of 6.5 years in Server Administration and DevOps"
        elif request.args.get("q") == "Degree":
            return "AS in Electronic Engineering & AS in Information Systems and Technologies"
        elif request.args.get("q") == "Email Address":
            return "madisona.mail@gmail.com"
        elif request.args.get("q") == "Phone":
            return "(347) 593-2765"
if __name__ == '__main__':
    app.run(host='0.0.0.0')
