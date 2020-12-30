class Passport:

    def __init__(self, passport_string: str):
        passport_string = passport_string.replace("\n", " ")
        field_values = passport_string.split(" ")
        self.fields = {field.split(":")[0]: field.split(":")[1] for field in field_values}

    def __str__(self):
        return f"{self.fields}"

    def is_valid(self):
        return self.__has_required_fields() and self.__is_valid_byr() and self.__is_valid_iyr() and self.__is_valid_eyr() \
               and self.__is_valid_hgt() and self.__is_valid_hcl() and self.__is_valid_ecl() and self.__is_valid_pid()

    def __has_required_fields(self):
        return "byr" in self.fields and "iyr" in self.fields and "eyr" in self.fields and "hgt" in self.fields and \
               "hcl" in self.fields and "ecl" in self.fields and "pid" in self.fields

    def __is_valid_byr(self):
        byr = self.fields["byr"]
        return len(byr) == 4 and str(byr).isnumeric() and int(byr) in range(1920, 2003)

    def __is_valid_iyr(self):
        iyr = self.fields["iyr"]
        return len(iyr) == 4 and str(iyr).isnumeric() and int(iyr) in range(2010, 2021)

    def __is_valid_eyr(self):
        eyr = self.fields["eyr"]
        return len(eyr) == 4 and str(eyr).isnumeric() and int(eyr) in range(2020, 2031)

    def __is_valid_hgt(self):
        hgt = str(self.fields["hgt"])
        if hgt.endswith("cm") or hgt.endswith("in"):
            number = hgt[:-2]
            return int(number) in range(150, 194) if hgt.endswith("cm") else int(number) in range(59, 77)
        return False

    def __is_valid_hcl(self):
        hcl = str(self.fields["hcl"])
        allowed = list("abcdef0123456789")
        return len(hcl) == 7 and hcl.startswith("#") and all(c in allowed for c in hcl[1:])

    def __is_valid_ecl(self):
        ecl = str(self.fields["ecl"])
        allowed = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return ecl in allowed

    def __is_valid_pid(self):
        pid = str(self.fields["pid"])
        return len(pid) == 9 and pid.isnumeric()


def get_passports(filename):
    with open(filename, 'r') as file:
        text = file.read()
        passports = text.split("\n\n")
        return [Passport(passport) for passport in passports]


def get_valid_passports(passports):
    return [passport for passport in passports if passport.is_valid()]


# passports = get_passports("resources/day4_test.txt")
passports = get_passports("resources/day4_input.txt")
valid_passports = get_valid_passports(passports)
# for p in valid_passports:
#     print(p)
print(len(valid_passports))
