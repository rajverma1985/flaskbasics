from flask import Flask, jsonify, request, Response
import json
app = Flask(__name__)

laptops = [
    { 'name': 'Inspiron',
      'price': 1499,
      'type': 'Home',
      'company': 'Dell',
      'ID': 1209878
    },
    {
      'name': 'Alienware',
      'price': 1899,
      'type': 'Gaming',
      'company': 'Dell',
      'ID': 6826103
    }
]


#updating the laptop information

@app.route('/laptops/<int:ID>', methods=['PUT'])
def put_laptops(ID):
    request_data=request.get_json()
    updated_laptop={
    "company": request_data['company'],
    "name": request_data['name'],
    "price": request_data['price'],
    "type": request_data['type'],
    "ID": ID
    }
    i=0
    for n in laptops:
        currentID= n["ID"]
        if currentID == ID:
            laptops[i]=updated_laptop
        i += 1
        response=Response("",status=204,)
    return response


#PTACH request to update only one record

@app.route('/laptops/<int:ID>', methods=['PATCH'])
def patch_laptops(ID):
    request_data=request.get_json()
    patched_laptop = {}
    if("name" in request_data):
        patched_laptop["name"]=request_data['name']
    for n in laptops:
        if n['ID']==ID:
            n.update(patched_laptop)
    response= Response("", status=204)
    response.headers['Location']= "laptops/" + str(ID)
    return response

    return jsonify(patched_laptop)



#post a new laptop information and add it to the list
@app.route('/laptops', methods=['POST'])
def add_laptop():
    varlaptop=request.get_json()
    if validobject(varlaptop):
        new_laptop={
        'name': varlaptop['name'],
        'price': varlaptop['price'],
        'type': varlaptop['type'],
        'company':varlaptop['company'],
        'ID':varlaptop['ID']
        }
        laptops.insert(0, varlaptop)
        response = Response("", 201, mimetype='application/json')
        response.headers['Location']= "/laptops/"+str(new_laptop['ID'])
        return response
    else:
        Invalidobject={
        "error": "This is an invalid object",
        "Help_msg": "please input data in the format {name': 'thinkpad', 'price': 99.99, 'type': 'home', 'company': 'hp', 'ID': '659715239'}"
        }
        response = Response(json.dumps(Invalidobject), status=400, mimetype='application/json')
        return response

#sanitize the data and not accept garbage data

def validobject(object):
    if 'name' in object and 'price' in object and 'type' in object and 'company' in object and 'ID' in object:
        return True
    else:
        return False

#GET laptop information
@app.route('/laptops')
def get_laptops():
    return jsonify({'laptops':laptops})

@app.route('/')
def get_hello():
    return 'Hello World'

#get laptop info based on #

@app.route('/laptops/<int:ID>')
def get_laptop_id(ID):
    return_value = {}
    for n in laptops:
        if n["ID"] == ID:
            return_value={
            'name':n["name"],
            'price':n["price"],
            'company':n["company"],
            'type':n['type']
            }
    return jsonify(return_value)

#GET laptop info based on the type
@app.route('/laptops/<type>')
def get_laptop_type(type):
    return_value = {}
    for n in laptops:
        if n["type"] == type.capitalize():
            return_value={
            'name':n["name"],
            'price':n["price"],
            'company':n["company"],
            'ID':n['ID']
            }
    return jsonify(return_value)


@app.route('/laptops/<int:ID>', methods=['DELETE'])
def delete_laptop(ID):
    i=0
    for n in laptops:
        if n["ID"]==ID:
            laptops.pop(i)
        i+=1
    return ""

app.run(port=5000)
