def check_pwd(pwd):
    if pwd:
        if len(pwd) < 8:
            return False
        else:
            return True
    return False
