import csv, statistics

class Utilities:
    #  Initial method to read csv file from the specified location
    # THIS COULD BE OPTIMIZED BY USING CATCHE METHOD
    def __init__(self):
        data = []
        with open('./take_home_assignment_data.csv', encoding='utf-8') as csvFile:
            csvData = csv.DictReader(csvFile)
            for rows in csvData:  
                data.append(rows)
                self.data = data


    # To get list of all pupils
    def getPupilList(self):
        return self.data
    
    # To get list of all pupil by grade
    def getGradeList(self, grade):
        data = [ item for item in self.data if item['grade'] == grade ]
        return data

    #get list of all pupil by pupil_id
    def getPupilScore(self, id):
        data = [ item for item in self.data if item['pupil_id'] == id ]
        return data

    # get avg amd median score of pupins based on filters

    def getMeanByGrade(self, parameters):
        try:
            data = self.data
            for key, val in parameters.items():
                if key == 'min_score':
                    data = [item for item in data if int(item['score']) >= int(val)]
                elif key == 'max_score':
                    data = [item for item in data if int(item['score']) <= int(val)]
                elif key == 'min_date':
                    data = [item for item in data if item['date'] >= val]
                else:
                    data = [item for item in data if item[key] == val]
                 
            data = [int(item['score']) for item in data]
            if data:
                median = statistics.median(data)
                average = sum(data)/len(data)
                return {'average': round(average, 2), 'median': median}
            else:
               return {'message': 'No matched data found'} 
        except Exception as ex:
            return {'message': 'Something Went Wrong!'}
        
        