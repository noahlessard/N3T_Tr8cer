class host_object:
    # this will all stay public so don't worry about setters
    whoisInfo = ""
    portInfo = []
    spamInfo = ""
    address = ""

    # parsing address will come later, don't worry about if its a range or not yet?
    def __init__(self, host_object, address):
        host_object.address = address

