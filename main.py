from collections import Counter

int_list = []
weights = {
    'R': 156,
    'N': 114,
    'D': 115,
    'C': 103,
    'E': 129,
    'Q': 128,
    'G': 57,
    'H': 137,
    'I': 113,
    'L': 113,
    'K': 128,
    'M': 131,
    'F': 147,
    'P': 97,
    'S': 87,
    'T': 101,
    'W': 186,
    'Y': 163,
    'V': 99,
    'A': 71}

#intial list function
def Intial_list(spectrum):
    counter = 0
    stop = 0
    temp = []
    new_weights = {}
    for k, v in weights.items():
        new_weights[v] = k
    length = len(spectrum)
    masses = list(new_weights.keys())
    aminoacids = list(new_weights.values())
    for index in range(0, length):
        for j in masses:
            if j == spectrum[index]:
                temp.append(j)
                counter += 1
                for v in aminoacids:
                    if v not in int_list:
                        if stop != counter:
                            int_list.extend(new_weights[temp[stop]])
                            stop += 1
    uniqueList = dict.fromkeys(int_list)
    intlist1 = list(uniqueList)
    return intlist1, counter

#linear spectrum function
def LinearSpectrum(peptide):
    sublist = []
    for i in range(1, len(peptide)):
        for j in range(0, len(peptide) - i + 1):
            sublist.append(peptide[j:j + i])
    #print(sublist)
    totals = [0]
    for i in sublist:
        totals.append(weight(i))
        # the totals list must be sorted
    sortedTotals = sorted(totals)
    return sortedTotals

#function take each element in the sublist to calculate the weight
def weight(subpeptide):
    total=0
    for s in subpeptide:
        total+=weights[s]
    return total

# Main
# peptide = input("Enter the Peptide: ")
# print(LinearSpectrum(peptide))
def isConsistent(Theoretical_Spectrum, subpeptide):
  #call linear spectrum
    peptides = LinearSpectrum(subpeptide)
    temp_spectrum = Theoretical_Spectrum.copy()
    peptides_count = len(peptides)-1
    spectrum_count = 0
    for p in peptides[1:]:
        if p in temp_spectrum:
            temp_spectrum.remove(p)
            spectrum_count+=1
    if spectrum_count == peptides_count:
        return True
    else:
        return False

#main function to call intial list and isConsistent
def main(spectrum):
    int_list, counter = Intial_list(spectrum)
    temp_list = int_list
    loop =1
    while loop < counter:
        final_list = []
        length1 = len(temp_list)
        length2 = len(int_list)
        for b in range(length1):
            for c in range(length2):
                result = ""
                t1=temp_list[b]
                t2 =int_list[c]

                result += t1
                result += t2
                valid= isConsistent(spectrum, result)
                if (valid):
                    final_list.append(result)
        loop +=1
        temp_list = final_list
    print(temp_list)
    print(counter)
#output main function

inputList = input("enter spectrum elements speratd by space: ")
list1 = inputList.split()
list2 = list(map(int, list1))

print(main(list2))
#0 97 97 99 101 103 196 198 198 200 202 295 297 299 299 301 394 396 398 400 400 497