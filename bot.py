import bottle
from urllib import parse, request

from common.credentials import tg_url_recruiter, tg_url_debug


# endpoint
@bottle.get('/')
def main():
    data = bottle.request.json
    print(data)
    r1 = request.urlopen(tg_url_debug.format(parse.quote(data["body"])))
    r2 = request.urlopen(tg_url_recruiter.format(parse.quote(data["body"])))

    return {"text": "answer"}


if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True)
