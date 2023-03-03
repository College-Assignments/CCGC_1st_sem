def ca_spaces(_str, length=22, price=False, mode="terminal"):
    # ca = calculate & append _spaces
    __str = str(_str)
    _seperator = " " if mode == "terminal" else "&nbsp;"
    if len(str(_str)) >= length:
        return _str
    if price:
        return str(_seperator * (length - len(__str) - 1)) + "$" + __str
    return str(_seperator * (length - len(__str))) + __str
