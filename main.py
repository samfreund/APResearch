import entropyCalc
import guessCalc
import json
import averager
import grapher

# ENSURE THAT ALL PATHS ARE MODIFIED TO ACCURATELY REFLECT LOCATIONS ON YOUR MACHINE

DATA_LOC = "/home/samf/gitClones/APResearch/data/output.json"
HASH_LOC = "/home/samf/gitClones/APResearch/resources/hashes/hashes.txt"

def main():
    data = json.load(open(DATA_LOC))

    # clear hashes file
    with open(
        HASH_LOC, mode="w"
    ) as hash_file:
        hash_file.write("")

    for datum in data:
        for key in datum["Passwords"]:
            password = datum["Passwords"][key]["Password"]
            entropy = entropyCalc.main(password)
            datum["Passwords"][key]["Entropy"] = entropy
            with open(
                HASH_LOC, mode="a"
            ) as hash_file:
                hash_file.write(password + "\n")

    guessCalc.main(DATA_LOC)

    json_data = json.dumps(data, indent=4)

    with open(
        DATA_LOC, mode="w"
    ) as json_file:
        json_file.write(json_data)

    averager.main(DATA_LOC)
    grapher.main(DATA_LOC)

if __name__ == "__main__":
    main()
