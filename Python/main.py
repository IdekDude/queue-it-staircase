import hashlib
import json
import base64

def SolveStaircase(input: str, zeroCount: int) -> tuple[str, str]:
    hash: str = hashlib.sha256(input.encode('utf-8')).hexdigest()
    
    ls: str = ''
    c: int = 1
    while c <= zeroCount:
        ls += "\\x20" * (zeroCount - c) + "#" * c

        if c != zeroCount:
            ls += ",\\x0a"

        c += 1

    return (
        hash, 
        base64.b64encode(json.dumps({"data": ls, "depth": zeroCount}).encode('utf-8')).decode('utf-8')
    )
