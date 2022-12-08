from flask import *
from dbmodel import *

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("/index.html")

@app.route("/about.html")
def about():
    return render_template("/about.html")

@app.route("/contact.html")
@app.route("/contact", methods=["POST","GET"])
def contact():
    if request.method == "POST":
        formdata = request.form
        contact = Contact(firstname=formdata.get('firstname'),
                          lasttname=formdata.get('laststname'),
                          email=formdata.get('email'),
                          phone=formdata.get('phone'),
                          message=formdata.get('message'))
        db.session.add(contact)
        db.session.commit()

    return render_template("/contact.html")



@app.route("/project.html")
def project():
    return render_template("/project.html")


@app.route("/blog_single.html")
def blog_single():
    return render_template("/blog_single.html")

@app.route("/service.html")
def service():
    return render_template("service.html")

if __name__ == '__main__':
    app.run(debug=True)