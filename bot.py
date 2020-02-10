import bottle
from urllib import parse, request

from common.credentials import tg_bot_url_recruiter, tg_bot_url_debug


# endpoint
@bottle.post('/')
def main():
    data = bottle.request.json
    print(data["body"])
    r1 = request.urlopen(tg_bot_url_debug.format(parse.quote(data["body"])))
    r2 = request.urlopen(tg_bot_url_recruiter.format(parse.quote(data["body"])))

    return r1


if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True)
