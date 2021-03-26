# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).
# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

# ips_between("10.0.0.0", "10.0.0.50")  ==   50 
# ips_between("10.0.0.0", "10.0.1.0")   ==  256 
# ips_between("20.0.0.10", "20.0.1.0")  ==  246


def ips_between(start, end):
    startList = [int(i) for i in start.split('.')]
    endList = [int(i) for i in end.split('.')]
    endValue = endList[3] + endList[2]*256 + endList[1] *(256**2) + endList[0] * (256**3)
    startValue = startList[3] + startList[2]*256 + startList[1] * (256**2) + startList[0] * (256**3)
    return endValue - startValue
