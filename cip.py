import random
import string

# engine
def main():
    dict = get_requirements()  # {"size":8, "Uppercase":1, "lowercase":5,"specials":2, "numbers":2}
    password = pswrd(dict)
    print(f"Here is the your required password-> {password}")


# asks user for requirements(size, uppercase and lowercase character count, special char count and numbers count)
def get_requirements():
    size = int(input("Enter password length: "))
    if size < 1:
        print("Password length must be at least 1. Please try again.")
        return get_requirements()
    if size > 100:
        print("Password length must not exceed 100 characters. Please try again.")
        return get_requirements()
    print(f"Available number of characters -> {size}")
    uppercase = int(input("Enter number of uppercase letters: "))
    print(f"Available number of characters -> {size - uppercase}")
    if uppercase < 0:
        print("Number of uppercase letters cannot be negative. Please try again.")
        return get_requirements()
    if uppercase > size:
        print("Number of uppercase letters exceeds total size. Please try again.")
        return get_requirements()
    if uppercase > size - 1:
        print("At least one character must be lowercase, special, or a digit. Please try again.")
        return get_requirements()
    lowercase = int(input("Enter number of lowercase letters: "))
    if lowercase < 0:
        print("Number of lowercase letters cannot be negative. Please try again.")
        return get_requirements()
    if lowercase > size - uppercase:
        print("Number of lowercase letters exceeds available characters. Please try again.")
        return get_requirements()
    print(f"Available number of characters -> {size - uppercase - lowercase}")
    specials = int(input("Enter number of special characters: "))
    if specials < 0:
        print("Number of special characters cannot be negative. Please try again.")
        return get_requirements()
    if specials > size - uppercase - lowercase:
        print("Number of special characters exceeds available characters. Please try again.")
        return get_requirements()
    print(f"Available number of characters -> {size - uppercase - lowercase - specials}")
    numbers = int(input("Enter number of digits: "))
    if numbers < 0:
        print("Number of digits cannot be negative. Please try again.")
        return get_requirements()
    if numbers > size - uppercase - lowercase - specials:
        print("Number of digits exceeds available characters. Please try again.")
        return get_requirements()
    if uppercase + lowercase + specials + numbers > size:
        print("Sum of character types exceeds total size. Please try again.")
        return get_requirements()
    return {
        "size": size,
        "Uppercase": uppercase,
        "lowercase": lowercase,
        "specials": specials,
        "numbers": numbers
    }

# create a randomized password based on requirements using random library
def pswrd(requirements):
    chars = []
    chars += random.choices(string.ascii_uppercase, k=requirements["Uppercase"])
    chars += random.choices(string.ascii_lowercase, k=requirements["lowercase"])
    chars += random.choices(string.punctuation, k=requirements["specials"])
    chars += random.choices(string.digits, k=requirements["numbers"])
    remaining = requirements["size"] - len(chars)
    if remaining > 0:
        chars += random.choices(
            string.ascii_letters + string.digits + string.punctuation, k=remaining
        )
    random.shuffle(chars)
    return ''.join(chars)


if __name__ == "__main__":
    main()