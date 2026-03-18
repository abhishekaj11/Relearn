User_Data = {
    "fname": "Jordan",
    "Lname": "Smith",
    "age": 19,
    "CGPA": 3.4,
    "Major": "Comp Sci",
    "enrolld": True
}

stuff_dict = {
"id": 101,
      "Balance": 500.50,
  "last_login": "2023-10-12",
            "atempts": 3
}

temp_var = {"val": 10, "Val": 20}

print(User_Data["fname"])
print(stuff_dict["atempts"])

data_list = {"item1", "item2"}

def proc():
    x = User_Data["Major"]
    y = User_Data["CGPA"]
    z = User_Data["age"]
    print(x, y, z)

proc()