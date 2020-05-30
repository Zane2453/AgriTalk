import csv
import datetime

def extract_data(file):
    csvfile = open(file)
    data = csv.reader(csvfile)
    data_points = []
    for row in data:
        data_points.append(row)

    return data_points

if __name__ == "__main__":
    path = '/Users/zane/Desktop/碩一下檔案/個別研究/Bao5M25/Bao5M25-'

    start = datetime.datetime.strptime("01-05-2019", "%d-%m-%Y")
    end = datetime.datetime.strptime("30-04-2020", "%d-%m-%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

    idfs = ['SoilEC1', 'PH1']
    odfs = ['Nitrogen']
    for date in date_generated:
        day = str(date.day) if int(date.day) >= 10 else '0'+str(date.day)
        month = str(date.month) if int(date.month) >= 10 else '0' + str(date.month)
        year = str(date.year)
        print(month, day)
        for odf in odfs:
            SoilECs = extract_data(path + idfs[0] + '/' + year + month + day + '.csv')
            PH1s =  extract_data(path + idfs[1] + '/' + year + month + day + '.csv')
            num = len(SoilECs) if len(SoilECs) < len(PH1s) else len(PH1s)
            EC_or_PH = 'EC' if len(SoilECs) < len(PH1s) else 'PH'
            if SoilECs and PH1s:
                output = open(path + odf + '/' + year + month + day + '.csv', 'w', newline='')
                writer = csv.writer(output)
                for index in range(num):
                    N_demand = 13
                    EC = float(SoilECs[index][1]) / 1000
                    PH = float(PH1s[index][1])
                    N_uptake = (63.25260883 * EC ** 2 + 14.2131821 * EC + 0.179708645) * 10
                    if N_uptake < N_demand and PH > 5:
                        irrigate = N_demand - N_uptake
                    else:
                        irrigate = 0

                    if EC_or_PH == 'EC':
                        writer.writerow([SoilECs[index][0], irrigate])
                    elif EC_or_PH == 'PH':
                        writer.writerow([PH1s[index][0], irrigate])