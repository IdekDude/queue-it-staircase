use sha2::{Sha256, Digest};
use base64::encode;
use serde_json::json;

fn solve_stair_case(input_data: &str, zero_count: usize) -> (String, String) {
    let mut hasher = Sha256::new();
    hasher.update(input_data);
    let hash = hasher.finalize();

    let mut ls = vec![];
    let mut c: usize = 1;
    while c <= zero_count {
        ls.push("\\x20".repeat(zero_count - c));
        ls.push("#".repeat(c));

        if c != zero_count {
            ls.push(",\\x0a".to_owned());
        }
        c += 1
    }

    let data = json!({
        "data": ls.concat(),
        "depth": zero_count
    });
    
    return (
        String::from(format!("{:x}", hash)),
        encode(data.to_string())
    );
}
