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

    # def calculate_guesses(password):
    guessCount = 0

    for hashcat in hashcats:
        # Start the subprocess
        process = subprocess.Popen(
            hashcat,  # Example command
            stdout=subprocess.PIPE,  # Capture the output
            stderr=subprocess.PIPE,  # Capture the error (optional)
            text=True,  # Decode output as text (Python 3.7+)
        )

        # Read stdout in real-time
        for line in process.stdout:
            guessCount += 1
            # print(line, end="")  # Print the output in real-time
            # print(str(guessCount) + "   " + password)

            if guessCount % 1000000000 == 0:
                print("\r" + str(guessCount) + "   " + password + str(hashcat), end="")

            if password == line.strip():
                return guessCount
        return -1


def main():
    # loop through json dict and then update with entropy values
    calculate_entropy("heyo")
    calculate_guesses()


if __name__ == "__main__":
    main()
