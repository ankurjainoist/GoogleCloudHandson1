# **Requirement:**

As a cloud specialist in a company, the company just decided to migrate its entire Data center to Google Cloud in 3 months. Manager decided that project will be divided in 2 stages:

Lift and Shift --> Migrate the Talent Management Portal to GCE
Modernization --> After migration, mission is to modernize the portal for GKE using the Migrate for ANTHOS.

![image](https://user-images.githubusercontent.com/52160164/130364905-079577cd-9d29-4fbc-b820-f4b9a5a935e0.png)

# **Lift & Shift**

1. Create new project or Use existing project and validate if billing is enabled or not (if billing not enabled, you will not able to create any resources in the project) 
![image](https://user-images.githubusercontent.com/52160164/130365497-4ff02738-c894-4f72-aa35-48ac8c52e8af.png)

2. Enable below 3 API's in project

API & Services--> Dashboard --> Enable API e Services.

**Cloud Resource Manager API**
![image](https://user-images.githubusercontent.com/52160164/130365575-43b67c43-3ec5-4311-ad15-910ad652708a.png)

**Compute Engine API**
![image](https://user-images.githubusercontent.com/52160164/130365602-98aa16f0-8f5f-47be-bac5-b4d07a18d95c.png)

**Kubernetes Engine API**
![image](https://user-images.githubusercontent.com/52160164/130365648-3e85795a-29ae-4432-ab5c-cc7725a3c0da.png)

3. Setup the default project in cloud shell for which we have enabled the API's

**gcloud config set project prod-project-83573**

This will make the value in variable **$DEVSHELL_PROJECT_ID** set as prod-project-83573 as **project ID.** 

![image](https://user-images.githubusercontent.com/52160164/130365728-f514a194-8933-4217-badc-fece0103257e.png)

4. Setup the compute zone as us-west-1-a as default

**gcloud config set compute/zone us-west1-a**

![image](https://user-images.githubusercontent.com/52160164/130365830-a18bd674-a6a1-4d98-9a9f-ecc0a7ea564b.png)


5. Add the firewall rules to allow traffic on **HTTP** and **SSH ports**. 

**gcloud compute firewall-rules create allow-ssh --network default \--allow tcp:22 --source-ranges 0.0.0.0/0**

![image](https://user-images.githubusercontent.com/52160164/130365860-1b8e652e-27c0-46db-8609-6c92ab3468c7.png)

**gcloud compute firewall-rules create allow-http --network default \--allow tcp:80 --source-ranges 0.0.0.0/0**

![image](https://user-images.githubusercontent.com/52160164/130365889-9d04d028-e4da-4394-9c2f-2fb48d5929b6.png)


6. Create new VM by cloud shell only to perform the Lift and Shift 

**P.S.: Before run, copy the command to a notepad and remove all "\". After that, run the command**

**gcloud compute instances create app-01 --project=$DEVSHELL_PROJECT_ID \
--zone=us-west1-a --machine-type=n1-standard-1 --subnet=default \
--scopes="cloud-platform" --tags=http-server,https-server \
--image=ubuntu-minimal-1604-xenial-v20210119a --image-project=ubuntu-os-cloud \
--boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=app-01**

![image](https://user-images.githubusercontent.com/52160164/130365971-9c8b53dc-a336-4cf9-9f44-eec819f22d72.png)

7. Generating Key pair in VM and setting up the permission

**ssh-keygen -t rsa -f ~/.ssh/app-key -C [USERNAME]**

**chmod 400 ~/.ssh/app-key****

To check what is username

![image](https://user-images.githubusercontent.com/52160164/130366062-4d06b013-4b05-455d-8259-4bdd583772ba.png)

![image](https://user-images.githubusercontent.com/52160164/130366092-857b68c7-7e09-4d00-a722-6abbe728bebf.png)
![image](https://user-images.githubusercontent.com/52160164/130366112-ad920d39-daa3-4ab6-8472-9914b7833c85.png)


8. Importing the Key piar generated to Google Cloud

**gcloud compute config-ssh --ssh-key-file=~/.ssh/app-key**

![image](https://user-images.githubusercontent.com/52160164/130366213-d8ee981a-14c6-40a5-9869-ba7969263684.png)

9. Connect to new VM via SSH and run below commands

**sudo apt-get update && sudo apt-get install apache2 unzip -y** ==> This will install the new update. apache and unzip to new VM

![image](https://user-images.githubusercontent.com/52160164/130366272-91763a01-c020-45bb-a239-d14cfbde939a.png)

**cd /var/www/html**

![image](https://user-images.githubusercontent.com/52160164/130366327-893a8665-5eb8-4787-b231-1dff2be10002.png)


**sudo mv index.html index.html.bkp**

This will backup the old index.html page

![image](https://user-images.githubusercontent.com/52160164/130366356-9f4e471b-aba7-4584-8c39-9f3f757fbe32.png)

**sudo curl -O https://storage.googleapis.com/bootcamp-gcp-en/hands-on-compute-website-files-en.zip**

Copy the App to the GCE

**sudo unzip hands-on-compute-website-files-en.zip**

![image](https://user-images.githubusercontent.com/52160164/130366398-992b8a21-f3c4-4413-b593-560f220de9aa.png)

Change the permission

**sudo chmod 644 ***

**Copy the External IP of the Compute Engine created and access it via browser to validate if the Lift & Shift process was completed successfully.**

![image](https://user-images.githubusercontent.com/52160164/130366486-c2796f1e-ad0e-44c1-bae7-0dcd3ee72636.png)












