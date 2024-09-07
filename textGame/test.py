test = {"key1": {"key2": {"test1": None}},
        "key3": {"key4": {"test2": None}}}
keys = test.keys()
for x in keys:
    if x == "key1":
        keys = test[x].keys()
        for y in keys:
            print(y)