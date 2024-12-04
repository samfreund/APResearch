import json
import subprocess

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


def main(dataLoc):
    for hashcat in HASHCATS:
        subprocess.run(hashcat, check=True)

        #TODO: Make this work
        with open(
            "/home/samf/gitClones/APResearch/resources/hashes/out.txt", mode="r"
        ) as out_file:
            out = out_file.read()

        out = out.split("\n")

        data = json.load(open(dataLoc))

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
            dataLoc, mode="w"
        ) as json_file:
            json_file.write(json_data)

if __name__ == "__main__":
    main()