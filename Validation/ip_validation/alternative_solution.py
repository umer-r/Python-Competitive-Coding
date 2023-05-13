def validate_ip(ip):
    part = ip.split(".")
    if not (len(part) == 4):
        return False
    for i in part:
        if int(i) > 255:
            return False
        if not isinstance(int(i),int):
            return False
    return True
    
if __name__ == "__main__":
    ip = "10.10.101.40"
    out = validate_ip(ip)
    if out:
        print(f"{ip} is valid IP.")
    else:
        print(f"{ip} is invalid IP.")