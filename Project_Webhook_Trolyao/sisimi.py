import requests
import json
def main(mess):
    ins = mess
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': '8LIQGLEpIGNZShpeWJd4HjVB40PoZwt0wWdZCvtO',
        # 'x-api-key':"ef2ba992-acba-4fe1-95f8-f4bb937e712f",
    }
    data1 = '{\n            "utext": "ins", \n            "lang": "vn" \n     }'
    data = data1.replace('"ins"','"{}"'.format(ins))
    encoded_data = data.encode("utf-8")

    response = requests.post('https://wsapi.simsimi.com/190410/talk', headers=headers, data=encoded_data)
    x = json.loads(response.text)
    str = x["atext"]
    return str