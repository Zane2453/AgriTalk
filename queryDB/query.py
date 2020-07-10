import os
import db
import models
from datetime import datetime 

db.connect()
s = db.get_session()
#filepath = r'./data/'

def queryData (fieldName, sensorName, timeY, timeM):

    filepath = './/'+ fieldName +'-'+ sensorName + '//'   
    if not os.path.isdir(filepath): os.system('mkdir ' + fieldName +'-'+ sensorName )

    for timeD in range(1,31):
        if timeM == '2' and timeD > 28: break
        startTime = timeY + '-' + timeM + '-' + str(timeD) + ' 00:00:00'
        endTime   = timeY + '-' + timeM + '-' + str(timeD) + ' 23:59:59'
        startOb = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
        endOb   = datetime.strptime(endTime  , '%Y-%m-%d %H:%M:%S')
        qData = (s.query(getattr(db.models, sensorName).timestamp, getattr(db.models, sensorName).value)
                 .select_from(getattr(db.models, sensorName))
                 .join(db.models.field)
                 .filter(db.models.field.name == fieldName)
                 .filter(getattr(db.models, sensorName).timestamp > startOb)
                 .filter(getattr(db.models, sensorName).timestamp < endOb)
                 .all())

        fp = open( filepath + timeY+timeM.zfill(2)+str(timeD).zfill(2) + '.csv' , 'w') 
        
        for entity in qData:
            fp.write(entity[0].strftime('%H:%M:%S')+ ', ' + str(entity[1]) + ',' + '\n')
        fp.close()



if __name__ == '__main__':
    #if os.path.isdir(filepath): os.system('rm '+ filepath + '*.csv')

    filedName = 'Bao5MM1'
    sensorName = 'UV1'

    queryData(filedName, sensorName, '2020', '1')
    queryData(filedName, sensorName, '2020', '2')
    queryData(filedName, sensorName, '2020', '3')
    queryData(filedName, sensorName, '2020', '4')
    queryData(filedName, sensorName, '2020', '5')
    queryData(filedName, sensorName, '2020', '6')
    queryData(filedName, sensorName, '2019', '1')
    queryData(filedName, sensorName, '2019', '2')
    queryData(filedName, sensorName, '2019', '3')    
    queryData(filedName, sensorName, '2019', '4')
    queryData(filedName, sensorName, '2019', '5')
    queryData(filedName, sensorName, '2019', '6')
    queryData(filedName, sensorName, '2019', '7')
    queryData(filedName, sensorName, '2019', '8')
    queryData(filedName, sensorName, '2019', '9')
    queryData(filedName, sensorName, '2019', '10')
    queryData(filedName, sensorName, '2019', '11')
    queryData(filedName, sensorName, '2019', '12')
    
    
