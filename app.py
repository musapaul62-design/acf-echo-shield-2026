import os, requests
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")
KOBO_BASE_URL = os.getenv("KOBO_BASE_URL", "https://eu.kobotoolbox.org").rstrip("/")
KOBO_ASSET_UID = os.getenv("KOBO_ASSET_UID", "ajcMeB4nsHXPoSdvbwGxRH")
KOBO_API_TOKEN = os.getenv("KOBO_API_TOKEN")

@app.get("/api/data")
def data():
    if not KOBO_API_TOKEN:
        return jsonify({"error":"KOBO_API_TOKEN is not configured on the server"}),500
    url=f"{KOBO_BASE_URL}/api/v2/assets/{KOBO_ASSET_UID}/data/"
    headers={"Authorization":f"Token {KOBO_API_TOKEN}","Accept":"application/json"}
    rows=[]
    try:
        while url:
            r=requests.get(url,headers=headers,timeout=60)
            r.raise_for_status()
            p=r.json()
            if isinstance(p,list): rows.extend(p); break
            rows.extend(p.get("results",[])); url=p.get("next")
        return jsonify({"count":len(rows),"results":rows})
    except requests.RequestException as e:
        return jsonify({"error":str(e)}),502

@app.route("/")
def index(): return send_from_directory("static","dashboard.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.getenv("PORT","5000")))
