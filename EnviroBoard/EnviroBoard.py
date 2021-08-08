from flask import Flask, render_template
from flask import jsonify
import scraper

app = Flask(__name__)
jobList = []

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/getjobs')
def getJobs():
    global jobList
    if len(jobList) == 0:
        jobList = scraper.infoscraper(scraper.linkscraper(scraper.pagedownload("https://www.goodwork.ca/volunteer/")))
    print(jobList)
    return jsonify(jobList)

if __name__ == "__main__":
    app.run(debug=True)
