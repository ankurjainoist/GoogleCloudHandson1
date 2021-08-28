**#  Requirement**

As a Cloud Specialist task to deploy Cloud Load Balancing between USA and Europe for high global availability and its smart traffic distributiion. 

![image](https://user-images.githubusercontent.com/52160164/131223950-de4209cd-57c6-461f-8d34-0046bac1cb61.png)

Before starting, make sure the enable below API's 

**Compute Engine API **

**Cloud Build API **

**Cloud Run API**

1. Download the KIDSFLIX app files and unzip it

**wget https://storage.googleapis.com/bootcamp-gcp-en/bootcamp-gcp-module-lb-files-app-usa.zip**

**wget https://storage.googleapis.com/bootcamp-gcp-en/bootcamp-gcp-module-lb-files-app-finland.zip**

**unzip bootcamp-gcp-module-lb-files-app-usa.zip**

**unzip bootcamp-gcp-module-lb-files-app-finland.zip**

# **FINLAND Deployment**

**Creating Container image and deploying via Cloud Run**

1. Access Finland application files

![image](https://user-images.githubusercontent.com/52160164/131224230-762ce4a8-581b-4b5f-970d-89fd07fddd18.png)

2. Running the Cloud Build in container image

**gcloud builds submit --tag gcr.io/$DEVSHELL_PROJECT_ID/appkidsflixfinland**

what above command does https://cloud.google.com/build/docs/running-builds/start-build-command-line-api#gcloud 

![image](https://user-images.githubusercontent.com/52160164/131224365-dbbf7f27-54be-43e5-98b5-aa687beaf174.png)

3. Deploying the application using the Cloud Run

**gcloud run deploy --image gcr.io/$DEVSHELL_PROJECT_ID/appkidsflixfinland --port 5000 --platform managed**

Select default name by pressing Enter appkidsflixfinland , region europe-north1 by typing number 13 and allow unauthenticated request by typing y

![image](https://user-images.githubusercontent.com/52160164/131224745-8838f1c5-b0d6-4763-a7ac-ea38e23df8d6.png)

![image](https://user-images.githubusercontent.com/52160164/131224791-f9219fa0-e9b8-4490-a4af-facd0c3bbf72.png)

# **USA Deployment**

**Creating Container image and deploying via Cloud Run**

1. Access USA application files

**cd ~/bootcamp-gcp-module-lb-files-app-usa**

![image](https://user-images.githubusercontent.com/52160164/131224853-d8c44f5b-d588-4e5d-88bd-b25102e330b0.png)

2. Running the Cloud Build in container image

**gcloud builds submit --tag gcr.io/$DEVSHELL_PROJECT_ID/appkidsflixusa**

what above command does https://cloud.google.com/build/docs/running-builds/start-build-command-line-api#gcloud 

![image](https://user-images.githubusercontent.com/52160164/131224933-a63b6c48-abcb-413e-a514-de2c9dc45e95.png)

3. Deploying the application using the Cloud Run

**gcloud run deploy --image gcr.io/$DEVSHELL_PROJECT_ID/appkidsflixusa --port 5000 --platform managed**

Select default name by pressing Enter appkidsflixfinland , region us-central1 by typing number 22 and allow unauthenticated request by typing y

![image](https://user-images.githubusercontent.com/52160164/131225097-3c139c08-3ce2-4b3c-8d6a-5746cdefc10a.png)

# **Deploying the HTTP Load Balancer**

1. Create 2 serverless Network End Point (NEG)

**gcloud compute network-endpoint-groups create sneg-appkidsflixfinland --region=europe-north1 --network-endpoint-type=serverless --cloud-run-service=appkidsflixfinland**

**gcloud compute network-endpoint-groups create sneg-appkidsflixusa --region=us-central1 --network-endpoint-type=serverless --cloud-run-service=appkidsflixusa**

![image](https://user-images.githubusercontent.com/52160164/131225446-a8954a46-80aa-4b78-9ec4-afa658c5d7ac.png)

2. Create BAckend service global

**gcloud compute backend-services create kidsflix-backend-global --global**

![image](https://user-images.githubusercontent.com/52160164/131225673-2ae1a739-e93d-4f29-89f9-1b498c728f36.png)

3. Adding serverless NEG created to backend service global

**gcloud compute backend-services add-backend kidsflix-backend-global --global --network-endpoint-group=sneg-appkidsflixfinland --network-endpoint-group-region=europe-north1**

**gcloud compute backend-services add-backend kidsflix-backend-global --global --network-endpoint-group=sneg-appkidsflixusa --network-endpoint-group-region=us-central1**

![image](https://user-images.githubusercontent.com/52160164/131225853-c9a71add-957a-48d1-a1e1-31b741fd04f5.png)

4. Create URL map to redirect the incoming requsition to backend service

**gcloud compute url-maps create lb-kidsflix-global --default-service kidsflix-backend-global**

![image](https://user-images.githubusercontent.com/52160164/131225914-c2c6d47c-bf6d-4b16-9361-ab6ecdcd918b.png)

5. Create the target HTTP proxy to redirect the requisition to ULR map

**gcloud compute target-http-proxies create lb-kidsflix-httpproxy --url-map=lb-kidsflix-global**

![image](https://user-images.githubusercontent.com/52160164/131225986-a28e0703-cb1f-4b05-9c7f-3d7a3b7b52af.png)

6. Reserving IP address to external Load Balancer

**gcloud compute addresses create kidsflix-global-ip --ip-version=IPV4 --global**

![image](https://user-images.githubusercontent.com/52160164/131226030-0dbce490-1812-4069-b0d6-c8ed325373db.png)

Now check the IP address kidsflix-global-ip

**gcloud compute addresses describe kidsflix-global-ip --format="get(address)" --global**

![image](https://user-images.githubusercontent.com/52160164/131226051-2dcd222e-8a66-42aa-a957-ac39441cb125.png)

7. Create global forwarding rule to redirect the incoming requsition to the proxy. 

**gcloud compute forwarding-rules create kidsflix-frontend-global \--address=kidsflix-global-ip \--target-http-proxy=lb-kidsflix-httpproxy \--global \--ports=80**

![image](https://user-images.githubusercontent.com/52160164/131226126-67a3957a-1f34-447d-bf41-790311c1972e.png)







































