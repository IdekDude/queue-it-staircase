const crypto = require('crypto')


async function SolveStaircase(input, zeroCount) {
    const hash = crypto.createHash("sha256").update(input).digest("hex");
    let ls = '';

    for (c = 1; c <= zeroCount; c++) {
        ls += "\\x20".repeat(zeroCount-c) + "#".repeat(c)
        if (c != zeroCount) {
            ls += ",\\x0a"
        }
    }

    return input, (btoa(JSON.stringify({"data": ls, "depth": zeroCount})))
};