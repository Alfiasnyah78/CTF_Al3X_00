from flask import Flask, request, render_template, make_response

app = Flask(__name__)

FLAG = "alx{c00ki3_Fr3y44_JKT48_0shi}"
DOB_CORRECT = "fff6927056a634ef2ee1e36e4498f814379887bee0b8a271de0e98635d4d35f415991aa12a46486f2ad4663b93043de2d46ebfdde2388cd45308aa493d27bcd3"

@app.route("/")
def index():
    dob = request.cookies.get("freya")
    show_flag = dob == DOB_CORRECT
    resp = make_response (render_template("index.html", flag=FLAG if show_flag else None))

    if not dob:
        resp.set_cookie("freya", "f99c5c986de6d31886633e6a5ec67e7cec8aeb9dcf2a150dd39db8c7099c8b3abeb458a7ded00b46f3778364bd91e0e1d7bf745e28da408a6eace7f2f275305e")

    return resp


@app.route("/reset")
def reset_cookie():
    resp = make_response(redirect("/"))
    resp.set_cookie("freya", "", expires=0)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2365, debug=True)

