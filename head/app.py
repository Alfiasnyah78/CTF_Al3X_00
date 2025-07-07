from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    flag = "alx{H3aed_5Sh0Tt_R3quest_812h7}"
    headers = request.headers

    lang = headers.get("Accept-Language", "")
   # xff = headers.get("X-Forwarded-For", "")
    referer = headers.get("Referer", "")
    user_agent = headers.get("User-Agent", "")

    msg = ""
    img_url = ""

    if "ja" not in lang:
        msg = "Bahasa! Harus Jepang."
        img_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZG9qNTNsdG5zNjJ2Z3FqNnI4b3Nla25jY2ZkM3JvdmNwZW1iMHpxeCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cXblnKXr2BQOaYnTni/giphy.gif"
    elif referer != "zoro":
        msg = "🧭 Refererensi harus dari pendekar pedang no 1 di one piece?"
        img_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmJ4eDNkdzRrZ29pczZiY3BvNXh4cWYxZmZmOGd5amhwY3JqZWV2NiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/4OV1bLOIWwIXRxpXlN/giphy.gif"
    elif "sanji" not in user_agent.lower():
        msg = "🍳 Belum kenalin Koki Bajak Laut Mugiwara.. bisa jadi dia agent"
        img_url = "https://media.giphy.com/media/4yfGy8lw0xnCU/giphy.gif?cid=ecf05e47mukall5k2dwf2e8ac9f1hwimudn59cuz6uhzpo84&ep=v1_gifs_search&rid=giphy.gif&ct=g"
    else:
        msg = "🎉 Monkey D. Luffy Bounty $5000000000000000000000000000000"
        img_url = "https://media.giphy.com/media/8Ep5103EzHQre/giphy.gif?cid=ecf05e47etdm43ov4shxlm7iy0hif3bn05g2uehpbj8v845c&ep=v1_gifs_search&rid=giphy.gif&ct=g"

        response = make_response(render_template("index.html", msg=msg, img_url=img_url))
        response.headers["X-Flag-Header"] = flag
        return response

    return render_template("index.html", msg=msg, img_url=img_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=90, debug=True)
