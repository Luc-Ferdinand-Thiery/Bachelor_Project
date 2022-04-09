import datetime
import json


import requests
from flask import render_template, redirect, request, Flask

app = Flask(__name__)
#port


# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"




votes = []
candidates = ["Candidate - 1", "Candidate - 2", "Candidate - 3"]


def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        print(chain)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        print(content)
        global votes
        votes = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)


@app.route('/')
def index():
    fetch_posts()
    return render_template('index.html',
                           title="Blockchain Network Voting",
                           votes=votes,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string,
                           x_cands=candidates,)


@app.route('/submit', methods=['POST'])
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """


    vote = request.form["VV"]

    post_object = {
        'vote': vote,
    }



    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')


if __name__ == '__main__':
   app.run(debug=True, port=5010)

