use std::str;

extern crate rot13;
extern crate base64;

fn main(){
  let cipher = "M3I6r2IbMzq9";
  let firstrot13 = rot13::rot13(cipher);
  let base64 = base64::decode(firstrot13).unwrap();
  let decodebase64  = String::from_utf8_lossy(&base64);
  let answer = rot13::rot13(&decodebase64);
  println!("Answer => {}", &answer);
}
