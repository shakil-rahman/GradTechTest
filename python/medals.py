medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]   

def createMedalTable(results):
    #Use the results object above to create a medal table
    #The winner gets 3 points, second place 2 points and third place 1 point
    medalTable = {}
    #Reversed so that the ordering matches the expected outcome
    for i in reversed(results):
        for countries in i['podium']:
            #Split the position and the country
            position = int(countries[:1])
            country = countries[2:]
            #Set default value for each country
            if country not in medalTable:
                medalTable[country] = 0
            #Add the points based on the position
            if position == 1:
                medalTable[country] += 3
            elif position == 2:
                medalTable[country] += 2
            elif position == 3:
                medalTable[country] += 1
        #Sorted on the value after the points for each event is processed
        medalTable = dict(sorted(medalTable.items(), key=lambda i: i[1], reverse=True))
    return medalTable


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable

test_function()
