#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
hospitalizedCurrently=$(echo $DATA | jq '.[0].hospitalizedCurrently')
death=$(echo $DATA | jq '.[0].death')


echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative COVID cases, $hospitalizedCurrently people currently hospitalized and $death total covid deaths."










