def introspection_info(obj):
    a = (type(obj))
    b = (dir(obj))
    c = (hasattr(obj, "obj"))
    d = (getattr(obj, 'a', "Упс"))
    e = (callable(obj))
    f = (isinstance(obj, str))
    return [a, b, c, d, e, f]


number_info = introspection_info(45)
print(number_info)

