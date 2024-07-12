d_child_1 = {"name":"George Orwell", "birth_date":1903}
d_child_1.update({"books":{"Homage to Catalonia 1938", "The Road to Wigan Pier 1937", "Nineteen Eighty-Four"}})
print(d_child_1)
d_child_2 = {"name":"Edgar Allan Poe", "birth_date":1809, "books":{"The Raven", "The Telltale Heart", "The Fall of the House of Usher"}}
d_parent = {"d1":d_child_1, "d2":d_child_2}
print("Mr. ", d_parent["d1"]["name"], "was born in ", d_parent["d1"]["birth_date"], "and is the author of the following books: \n", d_parent["d1"]["books"])
print("Mr. ", d_parent["d2"]["name"], "was born in ", d_parent["d2"]["birth_date"], "and is the author of the following books: \n", d_parent["d2"]["books"])
