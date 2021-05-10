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
        return True
    else:
        return False
