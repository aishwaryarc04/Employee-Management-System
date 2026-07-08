from flask import Flask, jsonify, request
from db import connect_db

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Employee Management API!"

@app.route("/employees", methods=["GET"])
def get_employees():

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(employees)

@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):

    data = request.get_json()

    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    UPDATE employees
    SET
        name=%s,
        age=%s,
        department=%s,
        designation=%s,
        salary=%s,
        phone=%s,
        email=%s
    WHERE emp_id=%s
    """

    values = (
        data["name"],
        data["age"],
        data["department"],
        data["designation"],
        data["salary"],
        data["phone"],
        data["email"],
        emp_id
    )

    cursor.execute(sql, values)
    conn.commit()

    if cursor.rowcount > 0:
        message = {"message": "Employee Updated Successfully"}
        status = 200
    else:
        message = {"message": "Employee not found"}
        status = 404

    cursor.close()
    conn.close()

    return jsonify(message), status

@app.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE emp_id=%s",
        (emp_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        message = {"message": "Employee Deleted Successfully"}
        status = 200
    else:
        message = {"message": "Employee not found"}
        status = 404

    cursor.close()
    conn.close()

    return jsonify(message), status

@app.route("/employees/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM employees WHERE emp_id=%s",
        (emp_id,)
    )

    employee = cursor.fetchone()

    cursor.close()
    conn.close()

    if employee:
        return jsonify(employee), 200
    else:
        return jsonify({"message": "Employee not found"}), 404

@app.route("/employees", methods=["POST"])
def add_employee():

    data = request.get_json()

    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    INSERT INTO employees
    (emp_id,name,age,department,designation,salary,phone,email)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        data["emp_id"],
        data["name"],
        data["age"],
        data["department"],
        data["designation"],
        data["salary"],
        data["phone"],
        data["email"]
    )

    cursor.execute(sql, values)

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message":"Employee Added Successfully"}),201

if __name__ == "__main__":
    app.run(debug=True)