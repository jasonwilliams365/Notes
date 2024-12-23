import re

pattern = r"\d+"

matches = re.findall(pattern, "There are 24 apples and 7 oranges")

print(matches)