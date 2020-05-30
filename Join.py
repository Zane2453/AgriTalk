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
    end = datetime.datetime.strptime("06-09-2019", "%d-%m-%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

    idfs = ['SoilEC1']
    odfs = ['N', 'K', 'P']
    for date in date_generated:
        day = str(date.day) if int(date.day) >= 10 else '0'+str(date.day)
        month = str(date.month) if int(date.month) >= 10 else '0' + str(date.month)
        year = str(date.year)
        print(month, day)
        for odf in odfs:
            SoilECs = extract_data(path + idfs[0] + '/' + year + month + day + '.csv')
            if SoilECs:
                output = open(path + odf + '/' + year + month + day + '.csv', 'w', newline='')
                writer = csv.writer(output)
                for SoilEC in SoilECs:
                    EC = float(SoilEC[1]) / 1000
                    if odf == 'K' or odf == 'P':
                        EC = round(31.62630442 * EC ** 2 + 7.106591065 * EC + 0.179854322, 3) * 10
                    elif odf == 'N':
                        EC = round(63.25260883 * EC ** 2 + 14.2131821 * EC + 0.179708645, 3) *10
                    writer.writerow([SoilEC[0], EC])