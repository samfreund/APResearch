import math
import subprocess
import json

# ENSURE THAT ALL PATHS ARE MODIFIED TO ACCURATELY REFLECT LOCATIONS ON YOUR MACHINE

# List of different attacks
HASHCATS = [
    [
        "hashcat",
        "-m",
        "99999",
        "/home/samf/gitClones/APResearch/resources/hashes/hashes.txt",
        "--outfile-format",
        "1,4",
        "-o",
        "/home/samf/gitClones/APResearch/resources/hashes/out.txt",
        "-a",
        "3",
        "?a?a?a?a?a?a?a?a",
        "--increment",
    ],  # Brute force
    [
        "hashcat",
        "-m",
        "99999",
        "/home/samf/gitClones/APResearch/resources/hashes/hashes.txt",
        "--outfile-format",
        "1,4",
        "-o",
        "/home/samf/gitClones/APResearch/resources/hashes/out.txt",
        "/home/samf/gitClones/APResearch/resources/wordlists/rockyou.txt",
        "-r",
        "/home/samf/gitClones/APResearch/resources/rules/OneRuleToRuleThemStill.rule",
    ],  # Rock you w/ OneRuleToRuleThemAll
]
GUESSES_PER_HASHCAT = [1, 2]  # TODO: Update with actual guesses per hashcat


def calculate_guesses():
    for hashcat in HASHCATS:
        subprocess.run(hashcat)

        #TODO: Make this work
        with open(
            "/home/samf/gitClones/APResearch/resources/hashes/out.txt", mode="r"
        ) as out_file:
            out = out_file.read()

        out = out.split("\n")

        data = json.load(open("/home/samf/gitClones/APResearch/data/output.json"))

        for datum in data:
            for key in datum["Passwords"]:
                guesses = int(datum["Passwords"][key]["Guesses"])
                password = datum["Passwords"][key]["Password"]
                cracked = False
                for line in out:
                    if password in line:
                        guesses += int(line.split(":")[1])
                        datum["Passwords"][key]["Guesses"] = guesses
                        cracked = True
                        break
                datum["Passwords"][key]["Cracked"] = cracked
                if not cracked:
                    guesses += GUESSES_PER_HASHCAT[HASHCATS.index(hashcat)]
                    datum["Passwords"][key]["Guesses"] = guesses

        json_data = json.dumps(data, indent=4)

        with open(
            "/home/samf/gitClones/APResearch/data/output.json", mode="w"
        ) as json_file:
            json_file.write(json_data)


def calculate_entropy(password):
    # Define the character sets
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = (
        "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"  # Common special characters
    )

    # Determine character set based on password content
    charset_size = 0
    if any(char in lowercase for char in password):
        charset_size += len(lowercase)
    if any(char in uppercase for char in password):
        charset_size += len(uppercase)
    if any(char in digits for char in password):
        charset_size += len(digits)
    if any(char in special_characters for char in password):
        charset_size += len(special_characters)

    # Calculate entropy per character
    if charset_size == 0:
        return 0  # No valid characters found
    entropy_per_char = math.log2(charset_size)

    # Total entropy
    total_entropy = entropy_per_char * len(password)

    return total_entropy


def main():
    data = json.load(open("/home/samf/gitClones/APResearch/data/output.json"))

    # clear hashes file
    with open(
        "/home/samf/gitClones/APResearch/resources/hashes/hashes.txt", mode="w"
    ) as hash_file:
        hash_file.write("")

    for datum in data:
        for key in datum["Passwords"]:
            password = datum["Passwords"][key]["Password"]
            entropy = calculate_entropy(password)
            datum["Passwords"][key]["Entropy"] = entropy
            with open(
                "/home/samf/gitClones/APResearch/resources/hashes/hashes.txt", mode="a"
            ) as hash_file:
                hash_file.write(password + "\n")

    calculate_guesses()

    json_data = json.dumps(data, indent=4)

    with open(
        "/home/samf/gitClones/APResearch/data/output.json", mode="w"
    ) as json_file:
        json_file.write(json_data)


if __name__ == "__main__":
    main()
