


def bl(attr_val):
    sndx_val = attr_val[0]  # Keep first letter
    for c in attr_val[1:]:  # Loop over all other letters

        if (c in 'aehiouwy'):  # Not inlcuded into Soundex code
            pass
        elif (c in 'bfpv'):
            if (sndx_val[-1] != '1'):  # Don't add duplicates of digits
                sndx_val += '1'
        elif (c in 'cgjkqsxz'):
            if (sndx_val[-1] != '2'):  # Don't add duplicates of digits
                sndx_val += '2'
        elif (c in 'dt'):
            if (sndx_val[-1] != '3'):  # Don't add duplicates of digits
                sndx_val += '3'
        elif (c in 'l'):
            if (sndx_val[-1] != '4'):  # Don't add duplicates of digits
                sndx_val += '4'
        elif (c in 'mn'):
            if (sndx_val[-1] != '5'):  # Don't add duplicates of digits
                sndx_val += '5'
        elif (c in 'r'):
            if (sndx_val[-1] != '6'):  # Don't add duplicates of digits
                sndx_val += '6'

    if (len(sndx_val) < 4):
        sndx_val += '000'  # Ensure enough digits

    sndx_val = sndx_val[:4]  # Maximum length is 4
    print(sndx_val)
bl('1989')
bl('@989')