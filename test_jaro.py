def jaro_comp(val1, val2):
    """Calculate the similarity between the two given attribute values based on
       the Jaro comparison function.

       As described in 'An Application of the Fellegi-Sunter Model of Record
       Linkage to the 1990 U.S. Decennial Census' by William E. Winkler and Yves
       Thibaudeau.

       Returns a value between 0.0 and 1.0.
    """

    # If at least one of the values is empty return 0
    #
    if (val1 == '') or (val2 == ''):
        return 0.0

    # If both attribute values exactly match return 1
    #
    elif (val1 == val2):
        return 1.0

    len1 = len(val1)  # Number of characters in val1
    len2 = len(val2)  # Number of characters in val2

    halflen = int(max(len1, len2) / 2) - 1

    assingment1 = ''  # Characters assigned in val1
    assingment2 = ''  # Characters assigned in val2

    workstr1 = val1  # Copy of original value1
    workstr2 = val2  # Copy of original value1

    common1 = 0  # Number of common characters
    common2 = 0  # Number of common characters

    for i in range(len1):  # Analyse the first string
        start = max(0, i - halflen)
        end = min(i + halflen + 1, len2)
        index = workstr2.find(val1[i], start, end)
        if (index > -1):  # Found common character, count and mark it as assigned
            common1 += 1
            assingment1 = assingment1 + val1[i]
    print(assingment1)
    for i in range(len2):  # Analyse the second string
        start = max(0, i - halflen)
        end = min(i + halflen + 1, len1)
        index = workstr1.find(val2[i], start, end)
        if (index > -1):  # Found common character, count and mark it as assigned
            common2 += 1
            assingment2 = assingment2 + val2[i]
    print(assingment2)

    if (common1 != common2):
        common1 = float(common1 + common2) / 2.0

    if (common1 == 0):  # No common characters within half length of strings
        return 0.0

    transposition = 0  # Calculate number of transpositions

    for i in range(len(assingment1)):
        if (assingment1[i] != assingment2[i]):
            print(assingment1[i],assingment2[i])
            transposition += 1
            print(transposition)
    transposition = transposition / 2.0


    common1 = float(common1)

    jaro_sim = 1. / 3. * (common1 / float(len1) + common1 / float(len2) + \
                          (common1 - transposition) / common1)

    assert (jaro_sim >= 0.0) and (jaro_sim <= 1.0), \
        'Similarity weight outside 0-1: %f' % (jaro_sim)

    return jaro_sim


jaro_comp('abcd', 'efgh')
