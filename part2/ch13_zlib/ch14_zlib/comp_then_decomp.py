import zlib
import json


def open_json_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return json.load(file)
        except ValueError as e:
            print('JSON 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None


json_object = open_json_file('..\\ch08_json\\message1.json')
json_str = json.dumps(json_object, ensure_ascii=False)
json_byte_data = json_str.encode('utf8')

# level은 1-9까지 지정이 가능합니다. 1은 가장 빠르나 압축률이 낮습니다.
# 9는 가장 느리나 압축률이 높습니다. 기본값 -1은 6과 동일합니다.
compressed_data = zlib.compress(json_byte_data, level=-1)
# 압축된 데이터의 CRC32 체크섬을 계산합니다.
crc32 = zlib.crc32(compressed_data)

print('\'json_str\' 데이터 길이={0}'.format(len(json_byte_data)))
print('압축된 \'compressed_json\' 데이터 길이={0}'.format(len(compressed_data)))
print('압축된 \'compressed_json\' 데이터 CRC2={0}'.format(crc32))

decompressed_data = zlib.decompress(compressed_data)
print('압축 해제된 \'decompressed_json\' 길이={0}'.format(len(decompressed_data)))
print('decompressed_data(UTF8)={0}'.format(decompressed_data.decode('utf8')))

