from flask import Flask, render_template, request, redirect, session
import json

app = Flask(__name__)
app.secret_key = "secret123"  # change later

# load tools
def load_tools():
    try:
        with open("tools.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_tools(data):
    with open("tools.json", "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    tools = load_tools()
    return render_template("index.html", tools=tools)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get("admin"):
        return redirect("/login")

    tools = load_tools()

    if request.method == "POST":
        name = request.form.get("name")
        desc = request.form.get("desc")
        link = request.form.get("link")

        tools.append({
            "name": name,
            "desc": desc,
            "link": link
        })
        save_tools(tools)

        return redirect("/admin")

    return render_template("admin.html", tools=tools)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "2267212474":
            session["admin"] = True
            return redirect("/admin")
        else:
            return "❌ Wrong username or password"

    return render_template("login.html")
    
@app.route("/rate", methods=["POST"])
def rate():
    name = request.form["name"]
    rating = int(request.form["rating"])
    review = request.form["review"]

    tools = load_tools()

    for tool in tools:
        if tool["name"] == name:
            tool.setdefault("rating", []).append(rating)
            tool.setdefault("reviews", []).append(review)

    save_tools(tools)
    return redirect("/")

@app.route("/fav/<name>")
def fav(name):
    favs = session.get("favs", [])

    if name not in favs:
        favs.append(name)

    session["favs"] = favs
    return redirect("/")

@app.route("/stats")
def stats():
    tools = load_tools()
    total_tools = len(tools)

    return {
        "total_tools": total_tools
    }

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)