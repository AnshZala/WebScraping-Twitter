from flask import Flask, render_template, jsonify
from twitter_scraper import scrape_twitter_trends
from proxy_manager import ProxyManager
from db_manager import DBManager
import os

app = Flask(__name__)

proxy_manager = ProxyManager('http://Anshzala12cloud:Anshzala12cloud@us-ca.proxymesh.com:31280')
db_manager = DBManager('mongodb://localhost:27017/')

@app.route('/')
def index():
    print(os.path.exists("templates/index.html"))  # Check if file exists
    return render_template('index.html')

@app.route('/run_script')
def run_script():
    proxy = proxy_manager.get_random_proxy()
    trends = scrape_twitter_trends(proxy)
    document = db_manager.insert_trends(trends, proxy)
    
    return jsonify({
        'dateTime': document['date'].isoformat(),
        'trends': trends,
        'ipAddress': document['ip_address'],
        'mongoRecord': document
    })

if __name__ == '__main__':
    app.run(debug=True)