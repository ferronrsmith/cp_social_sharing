from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/content/<content>')
@app.route('/content/<content>/image/<path:image>')
@app.route('/content/<content>/title/<title>')
@app.route('/content/<content>/image/<path:image>/title/<title>')
def load_meta(content, image=None, title='CarePass'):
    tags = {'title': title}
    if content is not None:
        tags['content'] = content
    if image is not None:
        tags['image'] = image
    else:
        tags['image'] = request.url_root + 'static/carepass-icon.png'

    return render_template('social.html', tags=tags, request=request)

if __name__ == '__main__':
    app.run()
