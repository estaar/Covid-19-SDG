def estimator(data):
    dataset = data
    def timeLapse():
        if data["periodType"] == "months":
            timelapse = data["timeToElapse"] * 30
        elif data["periodType"] == "weeks":
            timelapse = data["timeToElapse"] * 7
        else:
            timelapse = data["timeToElapse"]
        return timelapse

    def impacts():
        currentlyInfected = data["reportedCases"] * 10
        infectionsByRequestedTime = currentlyInfected * (2 ** int((timeLapse()/ 3)))
        severeCasesByRequestedTime = (15 / 100) * infectionsByRequestedTime
        hospitalBedsByRequestedTime = ((35 / 100) * data["totalHospitalBeds"]) - severeCasesByRequestedTime
        casesForICUByRequestedTime = (5 / 100) * infectionsByRequestedTime
        casesForVentilatorsByRequestedTime = (2 / 100) * infectionsByRequestedTime
        dollarsInFlight = (infectionsByRequestedTime * data["region"]['avgDailyIncomePopulation'] * data["region"][
          'avgDailyIncomeInUSD']) / data["timeToElapse"]

        # create impact dictionary
        impact = {"currentlyInfected": int(currentlyInfected),
                  "infectionsByRequestedTime": int(infectionsByRequestedTime),
                  "severeCasesByRequestedTime": int(severeCasesByRequestedTime),
                  "hospitalBedsByRequestedTime": int(hospitalBedsByRequestedTime),
                  "casesForICUByRequestedTime": int(casesForICUByRequestedTime),
                  "casesForVentilatorsByRequestedTime": int(casesForVentilatorsByRequestedTime),
                  "dollarsInFlight": int(dollarsInFlight),
                  }

        return impact
    def severeImpacts():
        currentlyInfected = data["reportedCases"] * 10
        infectionsByRequestedTime = currentlyInfected * (2 ** int((timeLapse()/ 3)))
        severeCasesByRequestedTime = (15 / 100) * infectionsByRequestedTime
        hospitalBedsByRequestedTime = ((35 / 100) * data["totalHospitalBeds"]) - severeCasesByRequestedTime
        casesForICUByRequestedTime = (5 / 100) * infectionsByRequestedTime
        casesForVentilatorsByRequestedTime = (2 / 100) * infectionsByRequestedTime
        dollarsInFlight = (infectionsByRequestedTime * data["region"]['avgDailyIncomePopulation'] * data["region"][
          'avgDailyIncomeInUSD']) / data["timeToElapse"]

        # create impact dictionary
        severeimpact = {"currentlyInfected": int(currentlyInfected),
                  "infectionsByRequestedTime": int(infectionsByRequestedTime),
                  "severeCasesByRequestedTime": int(severeCasesByRequestedTime),
                  "hospitalBedsByRequestedTime": int(hospitalBedsByRequestedTime),
                  "casesForICUByRequestedTime": int(casesForICUByRequestedTime),
                  "casesForVentilatorsByRequestedTime": int(casesForVentilatorsByRequestedTime),
                  "dollarsInFlight": int(dollarsInFlight),
                  }

        return severeimpact

    data = {"data": dataset, "impact": impacts(), "severeImpact": severeImpacts()}
    return data
