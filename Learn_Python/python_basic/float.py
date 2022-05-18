import decimal

print(round(1.115, 2))
print(round(1.125, 2))
print(round(1.135, 2))

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

IPV6_ADDRESS_LEN = 16
BASE = 256


def ipv6_address_add_num(ipv6_address, num):
    ipv6_address_copy = ipv6_address[:]
    index = IPV6_ADDRESS_LEN - 1
    while num and index >= 0:
        num_sum = ipv6_address_copy[index] + num
        ipv6_address_copy[index] = num_sum % BASE
        num = num_sum // BASE
        index = index - 1
    return ipv6_address_copy


if __name__ == '__main__':
    ipv6_address = [255, 254, 255, 255, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
    print(ipv6_address + [1])
    print(ipv6_address_add_num(ipv6_address, 1))
