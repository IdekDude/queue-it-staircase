import hashlib, base64, json


def solve_staircase(content, zero_count):
    gen_hash = hashlib.sha256()
    gen_hash.update(content.encode())
    gen_hash.digest()
    ls = ''

    for i in range(1, zero_count):
        ls += "\\x20" * (zero_count - i) + "#" * i
        if i != zero_count:
            ls += ",\\x0a"

    return gen_hash, (base64.b64encode(json.dumps({"data": ls, "depth": zero_count}).encode())).decode()

