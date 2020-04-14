def estimator(data):
    dataset = data
    def timeLapse():
        if data['periodType'] == 'months':
            timelapse = data['timeToElapse'] * 30
        elif data['periodType'] == 'weeks':
            timelapse = data['timeToElapse'] * 7
        else:
            timelapse = data['timeToElapse']
        timelapse = int(timelapse / 3)
        return timelapse
    def timeLapse1():
        if data['periodType'] == 'months':
            timelapse1 = data['timeToElapse'] * 30
        elif data['periodType'] == 'weeks':
            timelapse1 = data['timeToElapse'] * 7
        else:
            timelapse1 = data['timeToElapse']
        return timelapse1
    
    def impacts():
        currentlyInfected = data['reportedCases'] * 10
        infectionsByRequestedTime = currentlyInfected * (2 ** timeLapse())
        severeCasesByRequestedTime = int((15 / 100) * infectionsByRequestedTime)
        hospitalBedsByRequestedTime = int(((35 / 100) * data['totalHospitalBeds']) - severeCasesByRequestedTime)
        casesForICUByRequestedTime = int((5 / 100) * infectionsByRequestedTime)
        casesForVentilatorsByRequestedTime = int((2 / 100) * infectionsByRequestedTime)
        dollarsInFlight = int(infectionsByRequestedTime * data['region']['avgDailyIncomePopulation'] * data['region'][
          'avgDailyIncomeInUSD']) / timeLapse1())

        # create impact dictionary
        impact = {'currentlyInfected': int(currentlyInfected),
                  'infectionsByRequestedTime': int(infectionsByRequestedTime),
                  'severeCasesByRequestedTime': int(severeCasesByRequestedTime),
                  'hospitalBedsByRequestedTime': int(hospitalBedsByRequestedTime),
                  'casesForICUByRequestedTime': int(casesForICUByRequestedTime),
                  'casesForVentilatorsByRequestedTime': int(casesForVentilatorsByRequestedTime),
                  'dollarsInFlight': int(dollarsInFlight),
                  }

        return impact
    def severeImpacts():
        currentlyInfected = data['reportedCases'] * 50
        infectionsByRequestedTime = currentlyInfected * (2 ** timeLapse())
        severeCasesByRequestedTime = int((15 / 100) * infectionsByRequestedTime)
        hospitalBedsByRequestedTime = int(((35 / 100) * data['totalHospitalBeds']) - severeCasesByRequestedTime)
        casesForICUByRequestedTime = int((5 / 100) * infectionsByRequestedTime)
        casesForVentilatorsByRequestedTime = int((2 / 100) * infectionsByRequestedTime)
        dollarsInFlight = int(infectionsByRequestedTime * data['region']['avgDailyIncomePopulation'] * data['region'][
          'avgDailyIncomeInUSD']) / timeLapse1())

        # create impact dictionary
        severeimpact = {'currentlyInfected': int(currentlyInfected),
                  'infectionsByRequestedTime': int(infectionsByRequestedTime),
                  'severeCasesByRequestedTime': int(severeCasesByRequestedTime),
                  'hospitalBedsByRequestedTime': int(hospitalBedsByRequestedTime),
                  'casesForICUByRequestedTime': int(casesForICUByRequestedTime),
                  'casesForVentilatorsByRequestedTime': int(casesForVentilatorsByRequestedTime),
                  'dollarsInFlight': int(dollarsInFlight),
                  }

        return severeimpact

    data = {'data': dataset, 'impact': impacts(), 'severeImpact': severeImpacts()}
    return data
