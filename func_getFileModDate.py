def getLastMod(filename):
    if os.path.isfile(filename):
        return datetime.fromtimestamp(os.path.getmtime(file))
    else:
return datetime.fromtimestamp(0)