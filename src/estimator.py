def estimator(data):
    dataset = datasets
    if data["periodType"] == "months":
        tilelapse = data["timeToElapse"] * 30
    elif data["periodType"] == "weeks":
        timelapse == data["timeToElapse"] * 7
    else:
        timelapse = data["timeToElapse"]

    def impacts():
        currentlyInfected = data["reportedCases"] * 10
        infectionsByRequestedTime = currentlyInfected * (2 ** int((timelapse/ 3)))
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
        currentlyInfected = data["reportedCases"] * 50
        infectionsByRequestedTime = currentlyInfected * (2 ** int((timelapse / 3)))
        severeCasesByRequestedTime = (15 / 100) * infectionsByRequestedTime
        hospitalBedsByRequestedTime = ((35 / 100) * data["totalHospitalBeds"]) - severeCasesByRequestedTime
        casesForICUByRequestedTime = (5 / 100) * infectionsByRequestedTime
        casesForVentilatorsByRequestedTime = (2 / 100) * infectionsByRequestedTime
        dollarsInFlight = (infectionsByRequestedTime * data["region"]['avgDailyIncomePopulation'] * data["region"][
          'avgDailyIncomeInUSD']) / data["timeToElapse"]

        # Create severe impact dictionary
        severeImpact = {"currentlyInfected": int(currentlyInfected),
                        "infectionsByRequestedTime": int(infectionsByRequestedTime),
                        "severeCasesByRequestedTime": int(severeCasesByRequestedTime),
                        "hospitalBedsByRequestedTime": int(hospitalBedsByRequestedTime),
                        "casesForICUByRequestedTime": int(casesForICUByRequestedTime),
                        "casesForVentilatorsByRequestedTime": int(casesForVentilatorsByRequestedTime),
                        "dollarsInFlight": int(dollarsInFlight),

                        }
        return severeImpact
    data = {"data": datasets, "impact": impacts(), "severeImpact": severeImpacts()}
    return data
