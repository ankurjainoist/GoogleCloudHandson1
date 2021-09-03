# **Requirement: **

In link to the Module 5 project, after successfully migration of an application and database to Compute instances in Australia region, 
now the task is to modernize the same.

In this process, it will be necessary to migrate the resources that are running in the Google Compute Engine service to a Containerized Modern Architecture 
using the Google Kubernetes Engine and Cloud SQL services, with High Availability

![image](https://user-images.githubusercontent.com/52160164/132049424-97a470e2-a5e1-463e-b8f1-7d427ef6c17a.png)

Link to the old project where we migrate the APP and DB server from US to Australia: 
https://github.com/ankurjainoist/GoogleCloudHandson1/blob/main/Intercontinental_VM_migration.md 

1. Australia App and DB instances running 

![image](https://user-images.githubusercontent.com/52160164/132050093-eceb7e66-5442-4b4a-8101-f2becc0b689b.png)

2. Create SQL Instance in Autralia Region

![image](https://user-images.githubusercontent.com/52160164/132050286-01a3480b-4f5f-4ad0-8e7e-cfb1299ca4a0.png)

![image](https://user-images.githubusercontent.com/52160164/132050356-810efdab-760c-4bf5-8340-f3dc50544290.png)

![image](https://user-images.githubusercontent.com/52160164/132050860-c6b269cb-5446-4687-89ed-f26d19e52665.png)

**Cloud SQL Instance Created**

![image](https://user-images.githubusercontent.com/52160164/132052660-3e97ebf7-7041-4971-bf43-111717b53dae.png)

Create Database Clinic

![image](https://user-images.githubusercontent.com/52160164/132052796-b07c935e-e0ba-4d09-9ad9-e6ced93608cc.png)

Add new user "app"

![image](https://user-images.githubusercontent.com/52160164/132052933-d6046543-7aa2-4555-aada-a70a184f7664.png)


**3. Containrizing the Docker Application**

a. Open cloud shell

b. Download the App files

**wget https://storage.googleapis.com/bootcamp-gcp-en/bootcamp-gcp-module-db.zip**

**unzip bootcamp-gcp-module-db.zip**

![image](https://user-images.githubusercontent.com/52160164/132051419-b109afa3-38c3-4ce3-a29a-dfb669c98a4a.png)

c. Creating new image

**cd ~/bootcamp-gcp-module-db/app**

**docker build -t tcb-clinic-app .**

![image](https://user-images.githubusercontent.com/52160164/132051672-b1d062f6-3e4e-4303-8f16-d8f30c02d17e.png)

![image](https://user-images.githubusercontent.com/52160164/132051753-524e75ef-a70f-44fc-ba65-9975ee24e786.png)

d. Add tag and uploading it to container registery

**docker tag tcb-clinic-app asia.gcr.io/$DEVSHELL_PROJECT_ID/tcb-clinic-app:latest**

![image](https://user-images.githubusercontent.com/52160164/132051890-410f0e44-e19a-4c77-aa2b-de9810b57235.png)

**docker push asia.gcr.io/$DEVSHELL_PROJECT_ID/tcb-clinic-app:latest**

![image](https://user-images.githubusercontent.com/52160164/132051961-ccfca0da-2d2f-4220-a312-b602d1b4ed9a.png)

Now container registery created

![image](https://user-images.githubusercontent.com/52160164/132052082-d79629c7-f44f-4d0c-be75-763cf70a32ff.png)

**Now create Kubernetes Cluster**

![image](https://user-images.githubusercontent.com/52160164/132052332-64340c7d-82cc-41d1-81a9-2d833fcb91c2.png)

![image](https://user-images.githubusercontent.com/52160164/132052306-2f0c2c30-d870-4486-adbc-2f6e99cf8931.png)

Download yaml file having changes needed to deploy on Kubernetes cluster

**wget https://storage.googleapis.com/bootcamp-gcp-en/tcb-clinic.yaml**

![image](https://user-images.githubusercontent.com/52160164/132052539-195f84a6-c672-4289-8bd2-c4a0308a324b.png)

Edit yaml file : Edit the file tcb-clinic.yaml using the Cloud Editor, change the Private IP (DBHOST) of the CloudSQL:

![image](https://user-images.githubusercontent.com/52160164/132053631-e5036c17-ad54-4115-8387-192aed648aff.png)

![image](https://user-images.githubusercontent.com/52160164/132053733-ade3b38d-f625-483e-b5b0-caf9ae78fe57.png)

**Connecting to Kubernetes Cluster**

![image](https://user-images.githubusercontent.com/52160164/132054252-841dd536-30bf-410d-b8bb-e32b97578b40.png)

![image](https://user-images.githubusercontent.com/52160164/132054322-0f31f003-480b-4921-9116-0c5e34af38ea.png)

Deploy application using yaml file

**kubectl apply -f tcb-clinic.yaml**

![image](https://user-images.githubusercontent.com/52160164/132054445-427fe630-ea75-452a-8988-6cd4207257e2.png)

![image](https://user-images.githubusercontent.com/52160164/132054565-e4e350f7-2e0a-4ef1-b474-70e0d7837a5c.png)

![image](https://user-images.githubusercontent.com/52160164/132054590-86668137-db49-4b6c-ba3c-2dfe342e27e6.png)



**# Database migration Process**

Access DB instance via SSH

Load data into Aus-db
![image](https://user-images.githubusercontent.com/52160164/132057854-1918ec9e-2771-4034-a08f-4e7cf9b355ec.png)


1. Run below command to export data

**mysqldump --add-drop-table -u root -p clinic > clinic.sql**

![image](https://user-images.githubusercontent.com/52160164/132054859-d5d9ef2e-60cd-4eff-84fb-94d6ad4942b1.png)

![image](https://user-images.githubusercontent.com/52160164/132054978-23d217ec-4d4d-4219-94ae-cb1428cc851f.png)

**sed -e 's/utf8mb4_0900_ai_ci/utf8mb4_unicode_ci/g' -i clinic.sql**

**mysql -u app -p -h 10.112.176.2 clinic < clinic.sql**

![image](https://user-images.githubusercontent.com/52160164/132055241-483bc966-1b3c-4d2f-bd42-d480dc524c71.png)

![image](https://user-images.githubusercontent.com/52160164/132056806-dc161063-7be1-48b6-8812-76116a4a7a93.png)

**use clinic;**

**select * from patient;**

![image](https://user-images.githubusercontent.com/52160164/132057727-2af1d4eb-0ce7-4ed8-a532-4d7ee709cddb.png)

![image](https://user-images.githubusercontent.com/52160164/132057781-e96988aa-fe20-4f4a-933c-68e2fe87adef.png)

![image](https://user-images.githubusercontent.com/52160164/132058651-56cb3616-c2e2-41e8-b42f-9647073efc1d.png)

[Mod 7 Evidence.pdf](https://github.com/ankurjainoist/GoogleCloudHandson1/files/7108193/Mod.7.Evidence.pdf)






  




























