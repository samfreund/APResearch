import json
import sys
import matplotlib.pyplot as plt


def main(dataLoc):
    #Load json
    data = json.load(open(dataLoc))

    #Create graphs and store them in data/graphs

    #Graph 1: Scatterplot with entropy on the x-axis and guesses on the y-axis, color coded by cracked vs uncracked

    #Graph 2: Two boxplots, one for entropy of uncracked passwords and one for entropy of cracked passwords

    #Graph 3: Pie chart of cracked vs uncracked passwords

    #Graph 4: Bar graph comparing number of cracked passwords for different GPAs

    #Graph 5: Bar graph comparing number of cracked passwords for different grades

    #Graph 1
    entropy = []
    guesses = []
    cracked = []
    for datum in data:
        for key in datum["Passwords"]:
            entropy.append(datum["Passwords"][key]["Entropy"])
            guesses.append(datum["Passwords"][key]["Guesses"])
            cracked.append(datum["Passwords"][key]["Cracked"])
    #Create scatterplot
    fig, ax = plt.subplots()
    scatter = ax.scatter(entropy, guesses, c=cracked)
    ax.set_xlabel("Entropy")
    ax.set_ylabel("Guesses")
    ax.set_title("Entropy vs. Guesses")
    ax.legend(*scatter.legend_elements(), title="Cracked")
    ax.grid(True)
    fig.savefig("data/graphs/scatterplot.png")

    #Graph 2
    crackedEntropy = []
    uncrackedEntropy = []
    for datum in data:
        for key in datum["Passwords"]:
            if datum["Passwords"][key]["Cracked"]:
                crackedEntropy.append(datum["Passwords"][key]["Entropy"])
            else:
                uncrackedEntropy.append(datum["Passwords"][key]["Entropy"])
    #Create boxplot
    fig, ax = plt.subplots()
    ax.boxplot([uncrackedEntropy, crackedEntropy])
    ax.set_xticklabels(["Uncracked", "Cracked"])
    ax.set_ylabel("Entropy")
    ax.set_title("Entropy of Cracked vs. Uncracked Passwords")
    ax.grid(True)
    fig.savefig("data/graphs/boxplot.png")

    #Graph 3
    crackedPasswords = 0
    uncrackedPasswords = 0
    for datum in data:
        for key in datum["Passwords"]:
            if datum["Passwords"][key]["Cracked"]:
                crackedPasswords += 1
            else:
                uncrackedPasswords += 1
    #Create pie chart
    fig, ax = plt.subplots()
    ax.pie([crackedPasswords, uncrackedPasswords], labels=["Cracked", "Uncracked"], autopct="%1.1f%%")
    ax.set_title("Cracked vs. Uncracked Passwords")
    fig.savefig("data/graphs/piechart.png")

    #Graph 4
    crackedGPAs = {}
    for datum in data:
        if datum["Grade"] not in crackedGPAs:
            crackedGPAs[datum["Grade"]] = 0
        for key in datum["Passwords"]:
            if datum["Passwords"][key]["Cracked"]:
                crackedGPAs[datum["Grade"]] += 1
    #Create bar graph
    fig, ax = plt.subplots()
    ax.bar(crackedGPAs.keys(), crackedGPAs.values())
    ax.set_xlabel("Grade")
    ax.set_ylabel("Cracked Passwords")
    ax.set_title("Cracked Passwords by GPA")
    ax.grid(True)
    fig.savefig("data/graphs/bargraphGPA.png")

    #Graph 5
    crackedGrades = {}
    for datum in data:
        if datum["GPA"] not in crackedGrades:
            crackedGrades[datum["GPA"]] = 0
        for key in datum["Passwords"]:
            if datum["Passwords"][key]["Cracked"]:
                crackedGrades[datum["GPA"]] += 1
    #Create bar graph
    fig, ax = plt.subplots()
    ax.bar(crackedGrades.keys(), crackedGrades.values())
    ax.set_xlabel("GPA")
    ax.set_ylabel("Cracked Passwords")
    ax.set_title("Cracked Passwords by GPA")
    ax.grid(True)
    fig.savefig("data/graphs/bargraphGPA.png")




if __name__ == "__main__":
    main(sys.argv[1])