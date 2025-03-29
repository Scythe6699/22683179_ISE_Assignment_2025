def lucky_color(lpn):
    # lucky color dictionary
    color = {
        1: "Red",
        2: "Orange",
        3: "Yellow",
        4: "Green",
        5: "Sky Blue",
        6: "Indigo",
        7: "Violet",
        8: "Magenta",
        9: "Gold",
        11: "Silver",
        22: "White",
        33: "Crimson"
    }
    # Check if lpn is valid
    if lpn not in color:
        raise ValueError(f"Invalid Life Path Number: {lpn}")
    return color[lpn]