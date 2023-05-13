"""
    Task: check if ip string is valid
    Context: Juniper coding interview
    Category: Validation
    
    Problem statement: Write a Python program to validate if the given string is a valid IP address or not.

    Input: "10.10.101.40"
    Output: {ip} string is valid
"""
def validate_ip(ip):
    returner = ""
    ip_li = ip.split(".")
    if len(ip_li) > 4:
        returner += "False"
    for quad in ip_li:
        if int(quad) <= 255 and int(quad) >= 0:
            returner += "True"
        else:
            returner += "False"
    return returner

def validate_str(ip):
    str_rt = validate_ip(ip)
    if 'False' in str_rt:
        return False
    return True

if __name__ == "__main__":
    ip = "10.10.101.40"
    out = validate_str(ip)
    if out:
        print(f"{ip} is an valid IP.")
    else:
        print(f"{ip} is an invalid IP.")
