# app.py
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import markdown

app = Flask(__name__)

# Dados de exemplo para simular posts
posts = [
 #   {"id": 1, "title": "Post 1", "content": "Conteúdo do Post 1", "author": "Autor 1", "timestamp": datetime.now(), "comments": []},
 #   {"id": 2, "title": "Post 2", "content": "Conteúdo do Post 2", "author": "Autor 2", "timestamp": datetime.now(), "comments": []},
]

@app.route("/")
def index():
    # Ordena os posts por timestamp em ordem decrescente
    sorted_posts = sorted(posts, key=lambda x: x['timestamp'], reverse=True)
    return render_template("index.html", posts=sorted_posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post:
        # Renderiza a mensagem como Markdown
        post['content'] = markdown.markdown(post['content'], extensions=['markdown.extensions.fenced_code'])
        return render_template("post.html", post=post)
    return "Post não encontrado", 404

@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")

        new_post = {
            "id": len(posts) + 1,
            "title": title,
            "content": content,
            "author": author,
            "timestamp": datetime.now(),
        }
        posts.append(new_post)

        return redirect(url_for("index"))

    return render_template("create_post.html")

@app.route("/post/<int:post_id>/add_comment", methods=["POST"])
def add_comment(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)

    if post:
        comment_author = request.form.get("comment_author")
        comment_content = request.form.get("comment_content")

        new_comment = {
            "author": comment_author,
            "content": comment_content,
        }

        post["comments"].append(new_comment)

    return redirect(url_for("post", post_id=post_id))

if __name__ == "__main__":
    app.run(debug=True)

# Substitua app.run(debug=True) por app.run(host='0.0.0.0', port=81) para tornar o site público
