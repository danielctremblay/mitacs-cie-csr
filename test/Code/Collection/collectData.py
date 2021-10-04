

def parseSMM(file):

    with open(file, 'r') as fh:
        data = fh.readlines()[3:]

    cies_dict = {}

    for item in data:
        fields = item.split('\t')
         # TODO write in dict
        cie = {
            'symbol': fields[0],
            'name': fields[1],
            'exchange': fields[2],
            'symbol_cl': fields[3],
            'sector_gics': fields[4],
            'industry': fields[5],

        }

        print(fields[0])

    # if open('../../resources/cies/cec_listing.json', 'w+') as fh2:
    #     pass

if __name__ == '__main__':
    file_smm = '../../resources/cies/exchange_canadian.txt'

    parseSMM(file_smm)