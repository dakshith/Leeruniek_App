from rest_framework.response import Response
from rest_framework.decorators import api_view
from pupilScore.utilities import Utilities

@api_view(['GET'])
def index(request):
    urls={
        'By grade': 'http://www.127.0.0.1:8000/scores?grade=8',
        'By pupil_id': 'http://www.127.0.0.1:8000/scores?pupil_id=18',
        'By test_name': 'http://www.127.0.0.1:8000/scores?test_name=CITO_MATH',
        'By test_name':'http://www.127.0.0.1:8000/scores?test_name=CITO_MATH&min_score=15',
        'By minimum and maximum scores considered (inclusive)': 'http://www.127.0.0.1:8000/scores?test_name=CITO_MATH&min_score=15&max_score=20',
        'By minimum and maximum date considered (inclusive)': 'http://www.127.0.0.1:8000/scores?test_name=CITO_MATH&min_date=2019-01-01'
    }
    return Response(urls)
# list all the pupils that have taken a test in a grade
@api_view(['GET'])
def pupilList(request):
    pupilList = Utilities().getPupilList()
    return Response(pupilList)

#list the pupils that have taken a test in a specific grade
@api_view(['GET'])
def gradeList(request): 
    GradeList = Utilities().getGradeList(request.GET.get('grade'))
    return Response(GradeList)

#list of all the scores of a pupil
@api_view(['GET'])
def pupilScore(request):
    PupilScore = Utilities().getPupilScore(request.GET.get('pupil_id'))
    return Response(PupilScore)

"""
list the average and median value of all scores with the possibilities to add the following filters:
By grade http://www.127.0.0.1:8000/scores?grade=8
By pupil_id http://www.127.0.0.1:8000/scores?pupil_id=18
By test_name http://www.127.0.0.1:8000/scores?test_name=CITO_MATH
By test_name and grade  http://www.127.0.0.1:8000/scores?test_name=CITO_MATH&grade=5
By min score http://www.127.0.0.1:8000/scores?test_name=CITO_MATH&min_score=15
By minimum and maximum scores considered (inclusive) http://www.127.0.0.1:8000/scores?test_name=CITO_MATH&min_score=15&max_score=20
By minimum and maximum date considered (inclusive) http://www.127.0.0.1:8000/scores?test_name=CITO_MATH&min_date=2019-01-01
"""

@api_view(['GET'])
def scores(request):
    filterParameters = request.GET.dict()
    result = Utilities().getMeanByGrade(filterParameters)
    return Response(result)


