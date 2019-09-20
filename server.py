from flask import Flask, request, abort
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

oui_json = {}
with open('oui.json', 'r') as fp:
    oui_json = json.load(fp)

@app.route("/apiv3/hwaddress/search/<hwaddr>")
def hwaddr_search(hwaddr):
    referrer = request.headers.get("Referer")
    if 'https://hwaddress.noizze.net' not in referrer:
        return abort(400)

    separators = [':', '.', '-']
    for s in separators:
        hwaddr = hwaddr.replace(s, '')

    search_key = hwaddr[:6]
    return_value = { 'search_key': hwaddr, 'Assignment': search_key }
    return_value.update(oui_json[search_key])

    return json.dumps(return_value)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=4000, debug=True, threaded=True)

"""
import json
import csv

j = {}
with open('oui.csv') as fp:
    csv_data = csv.reader(fp)
    headers = next(csv_data, None)
    # print(headers)
    for l in csv_data:
        j[l[1]] = {'Organization Name': l[2], 'Organization Address': l[3]}

with open('oui.json', 'w') as fp:
    json.dump(j, fp)
"""
