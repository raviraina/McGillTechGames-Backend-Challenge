import json
from flask import Flask, request

app = Flask(__name__)
database = ['string1', 'string2']

# check
@app.route('/')
def home():
    return "works"

# return status
@app.route('/status')
def status():
    return {"status": "up"}

# echo path param
@app.route('/processPathData/<pathParameter>')
def processPathData(pathParameter):
    return {"pathParam" : f"{request.view_args['pathParameter']}"}

# process query 
@app.route('/processQueryData/')
def processQueryData():
    args = ()
    for r in request.args.lists():
        args = (r[0], r[1][0])

    return {
        "key" : f"{args[0]}",
        "value" : f"{args[1]}"
    }

# process post
@app.route('/processPOSTdata/')
def processPOSTdata():
    try:
        info = json.loads(request.data)
    except:
        return "Invalid data sent"
    
    vals = []
    for key in info:
        vals.append(info[key])

    return {"values: f'{vals}'"}

# get "database"/add to database
@app.route('/data', methods=['GET', 'POST'])
def data():
    if flask.request.method == 'GET':
        return str(database)
    else:
        try:
            info = json.loads(request.data)
        except:
            return "Invalid data sent"
        
        for key in info:
            database.append(info[key])

        return ('', 201)

# delete from database
@app.route('/data/<index>', methods=['DELETE']):
def delete(index):
    database.remove(index)
    return ('', 200)


if __name__ == '__main__':
    app.run(port=8080)

    