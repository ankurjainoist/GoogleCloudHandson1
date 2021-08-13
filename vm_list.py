import googleapiclient.discovery

#pass the project ID
PROJECT_ID="testing-project-322417"

compute = googleapiclient.discovery.build('compute', 'v1')
zones = compute.zones().list(project=PROJECT_ID).execute()
configs=[]
for zone in zones['items']:
    instances = compute.instances().list(project=PROJECT_ID, zone=zone['name']).execute()
    if 'items' in instances:
        for instance in instances['items']:
            configs.append(instance['name'])
print(configs)
