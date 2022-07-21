from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

# GET -> used to send data back
# POST -> used to receive data

stores=[
    {
        'name':'My Wonderful Store',
        'items':[
            {
            'name':'Chair',
            'price':4000
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST - /store data:{name:}
@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
    'name':request_data['name'],
    'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET - /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over the stores
    # If the Store is found return it
    # If not found display an error message
    for store in stores:
        if(store['name']==name):
            return jsonify(store)
    return jsonify({'Message':'Store Not Found!'})

# GET - /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

# POST - /store/<string:name>/item  data:{name:,price:}
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if(store['name']==name):
            new_item = {
            'name':request_data['name'],
            'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'Message':'Store not found!'})


# GET - /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if(store['name']==name):
            return jsonify({'items':store['items']})
    return jsonify({'Message':'Store not found!'})


app.run(port=5006)
