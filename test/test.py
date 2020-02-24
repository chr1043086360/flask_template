class App(object):
    NAME = "chr"


# print(dir(App))
con = {}


for key in dir(App):
    if key.isupper():
        con[key] = getattr(App, key)
print(con)
