from flask import Flask,request,jsonify
'''
Topic: Https methods

discussion:
    Http method define how client communicate with server.

'''



app=Flask(__name__)


# Demo employee data
employees = [
    {"id": 1, "name": "Arunesh", "salary": 50000, "age": 25},
    {"id": 2, "name": "Rahul", "salary": 60000, "age": 28},
    {"id": 3, "name": "Priya", "salary": 55000, "age": 26},
    {"id": 4, "name": "Sneha", "salary": 52000, "age": 24},
    {"id": 5, "name": "Rohan", "salary": 58000, "age": 27},
    {"id": 6, "name": "Anita", "salary": 53000, "age": 25},
    {"id": 7, "name": "Vikram", "salary": 61000, "age": 29},
    {"id": 8, "name": "Kavya", "salary": 54000, "age": 26},
    {"id": 9, "name": "Suman", "salary": 50000, "age": 24},
    {"id": 10, "name": "Nisha", "salary": 57000, "age": 27},
]


# 1️⃣GET 
""" user request the data from server"""
@app.route("/employee/<int:id>",methods=['GET'])
def emp_name(id):
    for emp in employees:
        if emp['id']==id:
            return jsonify({
                      "name": emp["name"],
                      "salary": emp["salary"],
                         "age": emp["age"]
                           })
        
    return 'no user founded'

#2️⃣ -------------------- POST create new employee --------------------
@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.json
    new_emp = {
        "id": data.get("id"),
        "name": data.get("name"),
        "salary": data.get("salary"),
        "age": data.get("age"),
    }
    employees.append(new_emp)
    return jsonify(new_emp), 201

# 3️⃣-------------------- PUT update existing employee --------------------
@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    emp = next((e for e in employees if e["id"] == id), None)
    if not emp:
        return {"error": "Employee not found"}, 404
    
    data = request.json
    emp["name"] = data.get("name", emp["name"])
    emp["salary"] = data.get("salary", emp["salary"])
    emp["age"] = data.get("age", emp["age"])
    return jsonify(emp)

# 4️⃣-------------------- DELETE an employee --------------------
@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    global employees
    employees = [e for e in employees if e["id"] != id]
    return {"message": f"Employee {id} deleted successfully"}

if __name__ == "__main__":
    app.run(debug=True)