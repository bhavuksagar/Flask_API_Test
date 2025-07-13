from flask import Flask,request


app=Flask(__name__)


items=[
    {
    "name":"coffee",
    "price":80
    },
    {
    "name":"Pasta",
    "price":180
    },
    {
    "name":"Tea",
    "price":50
    }
]

@app.get("/items")
def get_items():

    return {'items':items}


@app.post("/item")
def add_item():
    request_data=request.get_json()
    items.append(request_data)

    return {"Message":"Item added successfully"},201



@app.get("/item")
def get_item():
    name=request.args.get('name')
    for item in items:
        if name==item["name"]:
            return item
    return {"message":"Item Not found"},404


@app.put("/item")
def update_item():
    request_item=request.get_json()
    for i in items:
        if i["name"]==request_item["name"]:
            i["price"]=request_item["price"]
            return {"message":"Item Updated"}
    return {"message":"Item Not Found"},404


@app.delete("/item")
def delete_item():
    request_data=request.args.get("name")
    for i in items:
        if i["name"]==request_data:
            items.remove(i) 
            return {"message":"Item Deleted Successfully"} 
    return {"message":"Item not found"},404


'''

if main==__name__:
    app.run()

    '''