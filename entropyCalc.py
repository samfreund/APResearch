import math
import subprocess

# List of different attacks
hashcats = [
    [
        "hashcat",
        "-m",
        "99999",
        "/home/sam/gitClones/APResearch/resources/hashes/hashes.txt",
        "--outfile-format",
        "1,2,4",
        "-o",
        "/home/sam/gitClones/APResearch/resources/hashes/out.txt",
        "-a",
        "3",
        "?a?a?a?a?a?a?a?a",
        "--increment",
    ],  # Brute force
    [
        "hashcat",
        "-m",
        "99999",
        "/home/sam/gitClones/APResearch/resources/hashes/hashes.txt",
        "--outfile-format",
        "1,2,4",
        "-o",
        "/home/sam/gitClones/APResearch/resources/hashes/out.txt",
        "/home/sam/gitClones/APResearch/resources/wordlists/rockyou.txt",
        "-r",
        "/home/sam/gitClones/APResearch/resources/rules/OneRuleToRuleThemStill.rule",
    ],  # Rock you w/ OneRuleToRuleThemAll
]


def calculate_guesses():
    for hashcat in hashcats:
        subprocess.run(hashcat)


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
    # loop through json dict and then update with entropy values
    calculate_entropy("heyo")
    calculate_guesses()


if __name__ == "__main__":
    main()
