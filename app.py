from flask import Flask, request, jsonify

app = Flask(__name__)

# sample database
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET single user
@app.route("/users/<int:uid>", methods=["GET"])
def get_user(uid):
    for u in users:
        if u["id"] == uid:
            return jsonify(u)
    return jsonify({"error": "User not found"}), 404

# POST create user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data["name"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT update user
@app.route("/users/<int:uid>", methods=["PUT"])
def update_user(uid):
    data = request.get_json()
    for u in users:
        if u["id"] == uid:
            u["name"] = data.get("name", u["name"])
            return jsonify(u)
    return jsonify({"error": "User not found"}), 404

# DELETE user
@app.route("/users/<int:uid>", methods=["DELETE"])
def delete_user(uid):
    for u in users:
        if u["id"] == uid:
            users.remove(u)
            return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run()