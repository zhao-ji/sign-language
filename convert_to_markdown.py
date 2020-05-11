array = [
    ["4765", "mother"],
    ["4689", "father"],
    ["2111", "sister"],
    ["3513", "brother"],
    ["954", "child"],
    ["5389", "children"],
    ["4766", "parents"],
    ["4616", "uncle"],
    ["3687", "aunt"],
    ["5928", "nephew"],
    ["6275", "niece"],
    ["4204", "cousin"],
    ["1636", "family"],
    ["3338", "grandmother"],
    ["3337", "grandfather"],
    ["2184", "boy"],
    ["2135", "girl"],
    ["1231", "baby"],
    ["1083", "friend"],
    ["5982", "workmate"],
    ["3299", "partner"],
    ["2177", "boyfriend"],
    ["2131", "girlfriend"],
    ["2637", "engaged"],
    ["3055", "married"],
    ["2570", "single"],
    ["4524", "divorced"],
    ["4806", "alive"],
    ["483", "dead"],
    ["3027", "none"],
    ["1277", "pregnant"],
    ["3623", "famous"],
    ["1279", "before"],
    ["908", "now"],
    ["565", "live"],
    ["6180", "with"],
    ["2508", "alone"],
    ["1124", "dog"],
    ["4503", "cat"],
    ["751", "fish"],
    ["4508", "bird"],
    ["2832", "rabbit"],
    ["637", "pet"],
    ["2406", "city"],
    ["2729", "far"],
    ["810", "near"],
    ["5506", "how-old"],
    ["980", "older"],
    ["2645", "younger"],
    ["5818", "all"],
]


if __name__ == "__main__":
    for number, name in array:
        print (
            "|{name}|"
            "![{name}](https://www.nzsl.nz/images/signs/400-400"
            "/{number}/{name}-{number}-default.png)|"
            "[{name}](http://nzsl.vuw.ac.nz/signs/{number})|"
        ).format(name=name, number=number)
