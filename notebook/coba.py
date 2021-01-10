from ingredient_parser.en import parse 

print(type(parse('1 cup warm water (110 degrees F/45 degrees C)').get("name")))

# from recipe_searchers import search_recipe

# result = search_recipe("12 ounces lean ground beef, preferably 85 percent lean")
# print(f"Found results: \n {result}")

my_string="hello python world , i'm a beginner "
print (my_string.split(",",1)[1])
print (my_string.split("'",1)[1])