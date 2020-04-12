import json
def estimator(data):
    dataset = data
    def timeLapse():
        if data["periodType"] == "months":
            timelapse = data["timeToElapse"] * 30
        elif data["periodType"] == "weeks":
            timelapse = data["timeToElapse"] * 7
        else:
            timelapse = data["timeToElapse"]
        timelapse = int(timelapse / 3)
        return timelapse
    # print(timeLapse())

    def impacts():
        currentlyInfected = data["reportedCases"] * 10
        infectionsByRequestedTime = currentlyInfected * (2 ** timeLapse())
        # severeCasesByRequestedTime = int((15 / 100) * infectionsByRequestedTime)
        # hospitalBedsByRequestedTime = int(((35 / 100) * data["totalHospitalBeds"]) - severeCasesByRequestedTime)
        # casesForICUByRequestedTime = int((5 / 100) * infectionsByRequestedTime)
        # casesForVentilatorsByRequestedTime = int((2 / 100) * infectionsByRequestedTime)
        # dollarsInFlight = int((infectionsByRequestedTime * data["region"]['avgDailyIncomePopulation'] * data["region"][
        #   'avgDailyIncomeInUSD']) / data["timeToElapse"])

        # create impact dictionary
        impact = {"currentlyInfected": int(currentlyInfected),
                  "infectionsByRequestedTime": int(infectionsByRequestedTime),
                  # "severeCasesByRequestedTime": int(severeCasesByRequestedTime),
                  # "hospitalBedsByRequestedTime": int(hospitalBedsByRequestedTime),
                  # "casesForICUByRequestedTime": int(casesForICUByRequestedTime),
                  # "casesForVentilatorsByRequestedTime": int(casesForVentilatorsByRequestedTime),
                  # "dollarsInFlight": int(dollarsInFlight),
                  }

        return impact
    def severeImpacts():
        currentlyInfected = data["reportedCases"] * 10
        infectionsByRequestedTime = currentlyInfected * (2 ** timeLapse())
        # severeCasesByRequestedTime = int((15 / 100) * infectionsByRequestedTime)
        # hospitalBedsByRequestedTime = int(((35 / 100) * data["totalHospitalBeds"]) - severeCasesByRequestedTime)
        # casesForICUByRequestedTime = int((5 / 100) * infectionsByRequestedTime)
        # casesForVentilatorsByRequestedTime = int((2 / 100) * infectionsByRequestedTime)
        # dollarsInFlight = int((infectionsByRequestedTime * data["region"]['avgDailyIncomePopulation'] * data["region"][
        #   'avgDailyIncomeInUSD']) / data["timeToElapse"])

        # create impact dictionary
        severeimpact = {"currentlyInfected": int(currentlyInfected),
                  "infectionsByRequestedTime": int(infectionsByRequestedTime),
                  # "severeCasesByRequestedTime": int(severeCasesByRequestedTime),
                  # "hospitalBedsByRequestedTime": int(hospitalBedsByRequestedTime),
                  # "casesForICUByRequestedTime": int(casesForICUByRequestedTime),
                  # "casesForVentilatorsByRequestedTime": int(casesForVentilatorsByRequestedTime),
                  # "dollarsInFlight": int(dollarsInFlight),
                  }

        return severeimpact

    datas = {"data": dataset, "impact": impacts(), "severeImpact": severeImpacts()}
    data = json.dumps(datas)
    return data

# with open("G:\Covid-19-SDG\Datas.json", 'r') as mydata:
#   data = json.load(mydata)
#
# print(estimator(data))

# print(estimator(json.load("G:\Covid-19-SDG\Datas.json")))