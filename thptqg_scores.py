import requests
import json


def convert_to_vietnamese_string(data):
    def convert_key(key):
        vietnamese_mapping = {
            'sbd': 'Số báo danh',
            'toan': 'Điểm Toán',
            'van': 'Điểm Văn',
            'ngoaiNgu': 'Điểm Ngoại Ngữ',
            'vatLy': 'Điểm Vật Lý',
            'hoaHoc': 'Điểm Hóa Học',
            'sinhHoc': 'Điểm Sinh Học',
            'diemTBTuNhien': 'Điểm TB Tự Nhiên',
            'lichSu': 'Điểm Lịch Sử',
            'diaLy': 'Điểm Địa Lý',
            'gdcd': 'Điểm GDCD',
            'diemTBXaHoi': 'Điểm TB Xã Hội',
            'phoDiem': 'Phổ điểm',
            'top100': 'Top 100',
            'student': 'Student'
        }
        return vietnamese_mapping[key]

    result = {}
    for key, value in data.items():
        if key != 'sbd' and value == None:
            continue
        result[convert_key(key)] = value

    return result


def scoreLookup(identificationNumber: str):
    url = f'https://dantri.com.vn/thpt/1/0/99/{identificationNumber}/2023/0.2/search-gradle.htm'
    response = requests.get(url)
    data = convert_to_vietnamese_string(json.loads(response.text)['student'])

    if data['Số báo danh'] == None:
        return None

    result = str()
    for key, value in data.items():
        result += f'{key}: {value}\n'

    return result.strip()
