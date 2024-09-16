def introspection_info(obj):
    print(type(obj))
    print(dir(obj))
    print(hasattr(obj, "obj"))
    print(getattr(obj, 'a', "Упс"))
    print(callable(obj))
    print(isinstance(obj, str))


number_info = introspection_info(45)

