import * as crypto from 'crypto'

function SolveStaircase(input: string, zeroCount: number) {
    const hash = crypto.createHash("sha256").update(input).digest("hex");
    let ls = '';

    for (let c = 1; c <= zeroCount; c++) {
        ls += "\\x20".repeat(zeroCount - c) + "#".repeat(c)
        if (c != zeroCount) {
            ls += ",\\x0a"
        }
    }

    return { hash, data: (btoa(JSON.stringify({ "data": ls, "depth": zeroCount }))) }
}