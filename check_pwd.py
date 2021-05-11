def check_pwd(pwd):
    if pwd:
        if len(pwd) < 8 or len(pwd) > 20:
            return False
        if not any(p.isdigit() for p in pwd):
            return False
        if not any(p.islower() for p in pwd):
            return False
        if not any(p.isupper() for p in pwd):
            return False
        symbols = ["~", "`", "!", "@", "#", "$","%",
                   "^", "&", "*", "(", ")", "_", "+",
                   "-", "="]
        symExists = 0
        for p in pwd:
            if p in symbols:
                symExists = symExists + 1
        if symExists < 1:
            return False
        for p in pwd:
            if not p.isdigit() and not p.islower() and not p.isupper():
                if p not in symbols:
                    return False
                else:
                    pass
        return True
    else:
        return False
