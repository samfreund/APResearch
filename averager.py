import json


def main(dataLoc):
    # Loop through each datum, and average the entropy of each password, and guesses of each cracked password
    data = json.load(open(dataLoc))
    for datum in data:
        entropySum = 0
        crackedPasswords = 0
        guessAverage = 0
        for key in datum["Passwords"]:
            entropySum += datum["Passwords"][key]["Entropy"]
            if datum["Passwords"][key]["Cracked"]:
                crackedPasswords += 1
                guessAverage += datum["Passwords"][key]["Guesses"]
        datum["AverageEntropy"] = entropySum / len(datum["Passwords"])
        datum["AverageGuesses"] = guessAverage / crackedPasswords

    # Write the updated data to the file
    json_data = json.dumps(data, indent=4)

    with open(dataLoc, mode="w") as json_file:
        json_file.write(json_data)


if __name__ == "__main__":
    main()
