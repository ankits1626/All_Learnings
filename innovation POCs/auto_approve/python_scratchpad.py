def find_brand_by_code(code):
    brand_lookup = {
        "Alain Mikli": ["AO"],
        "Armani Exchange": ["AX"],
        "Burberry": ["BE", "JB"],
        "Chanel": ["CH"],
        "Coach": ["HC"],
        "Dolce & Gabbana": ["DG"],
        "Emporio Armani": ["EA", "EK"],
        "Giorgio Armani": ["AR", "GA"],
        "Michael Kors": ["MK"],
        "Miu Miu": ["MU"],
        "Oakley": ["OO", "SOK", "FOK", "OX", "OY", "OJF", "OK", "SOK", "OJ"],
        "Oliver Peoples": ["OV"],
        "Persol": ["PO"],
        "Prada": ["PR", "PS"],
        "Ray-Ban": ["RB", "RX", "RY", "RJ", "RW", "RJ"],
        "Starck Eyes": ["SH"],
        "Tiffany": ["TF"],
        "Versace": ["VE", "VK"],
        "Vogue": ["VO"],
        "Bvlgari": ["BV"],
        "Polo Ralph Lauren": ["PH"],
        "Swarovski": ["SK"],
        "Miraflex": ["MF"],
        "Jimmy Choo": ["JC"],
    }

    for brand, codes in brand_lookup.items():
        if code in codes:
            return brand
    return None


result = find_brand_by_code("JC")
print(result)  # Output: Ray-Ban

result = find_brand_by_code("XX")
print(result)  # Output: None