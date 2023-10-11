#![allow(unused)]

use std::fs::File;

pub fn add_item() {
     println!("add_item");
}

pub fn get_all() {}

//...

struct Csv {
     filename: String,
     file: File,
}

impl Csv {
     fn filename() {}

     //...
}