# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import boto3
import datetime

inNameSpc = 'AWS/DynamoDB'
inMetName = 'ProvisionedWriteCapacityUnits'
inDimensions = [{'Name': 'TableName','Value': 'usertable'},]
inStrtTime = '2018-3-23T16:45:00-07:00'
inEndTime = '2018-3-23T17:15:00-07:00'
inPeriod = 300
inStat = ['Average']
inUnit = 'Count'
region = 'us-west-1'
CUTotal = 0

cw = boto3.client('cloudwatch',region_name=region)

awsdata = cw.get_metric_statistics(
  Namespace=inNameSpc,
  MetricName=inMetName,
  Dimensions=inDimensions,
  StartTime=inStrtTime,
  EndTime=inEndTime,
  Period=inPeriod,
  Statistics=inStat,
  Unit=inUnit
)
awsdp = awsdata['Datapoints']
# print(awsdata.values())
for x in awsdp:
  CUTotal += x['Average']
print(awsdp)
print (CUTotal)
