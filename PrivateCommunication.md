**Requirement:**
As a Cloud Specialist, need to interconnect the AWS and GCP Architecture in Private way. 

![image](https://user-images.githubusercontent.com/52160164/129602899-e8ea3df0-1c20-4b82-b250-cb6d2ac8fda0.png)

**Pre requisite:**
1. Create AWS Tier Account
![image](https://user-images.githubusercontent.com/52160164/129603307-747bee7e-edef-4ed8-a6e7-186bab046fe0.png)

**Steps:**
1. Create New GCP Project and Add Billing account to same
![image](https://user-images.githubusercontent.com/52160164/129603814-4fa6a403-a0c7-43bc-ab78-988d53e19536.png)
Project ID: tcb-gcp-aws-007
Name: tcb-gcp-aws

2. Enable Compute Engine API using below link
https://console.cloud.google.com/flows/enableapi?apiid=compute_component,deploymentmanager&_ga=2.90885017.2003023334.1613150551-112422406.1602704538

![image](https://user-images.githubusercontent.com/52160164/129604810-398527e2-a51f-4936-9a52-0273a0319eac.png)

3. Run Command in cloudshell to download all project files to direct use the same in our project
curl -O https://storage.googleapis.com/bootcamp-gcp-public/hands-on-tcb-bmc-gcp.zip
![image](https://user-images.githubusercontent.com/52160164/129608050-0cb513f3-85ab-4c3c-aed5-ecfe9d0fb68f.png)

4. Unzip the ZIP file and accessing the same
unzip hands-on-tcb-bmc-gcp.zip
![image](https://user-images.githubusercontent.com/52160164/129608202-28a897ad-b964-43a7-8721-0efc66366378.png)
![image](https://user-images.githubusercontent.com/52160164/129608397-996d9e62-875c-458b-84fa-f9d3fed4855d.png)


5. Allowing execute permission for all files .sh
![image](https://user-images.githubusercontent.com/52160164/129608491-d7c188d7-1487-4fa4-8718-ce1b9730f7ef.png)

**Creating credentials in the GCP**
1. Downlaod the keys in JSON format for the Default Service Account i.e. Compute Engine Default Service account
 ![image](https://user-images.githubusercontent.com/52160164/129608955-dcc10132-0f5b-40d5-8b03-3eda718b7bcb.png)

2. Upload keys file and run ./gcp_set_credentials.sh ~/tcb-gcp-aws-007-7abd2c33035b.json
![image](https://user-images.githubusercontent.com/52160164/129611026-e2c5ae04-3c05-47f6-82af-8470a7cd57f0.png)
This will allow Terraform to access GCP to create the resources. 

**Creating Credentials in AWS**
1. Create User in IAM and provide Admin Access and download .csv file
![image](https://user-images.githubusercontent.com/52160164/129611885-652c4552-4aab-4a44-86ec-bf459d0331ef.png)

2. Upload the Keys to cloud shell and run ./aws_set_credentials.sh ~/accessKeys.csv
![image](https://user-images.githubusercontent.com/52160164/129612407-6a44da3b-9bc9-4964-9b0b-e9decf56223d.png)

**Getting TERRAFORM Ready**
1. Run command in the project where we have all terra form .sh files are present (downloaded in previous steps)
![image](https://user-images.githubusercontent.com/52160164/129613162-0cd7a8db-a30b-4f3d-a5f3-cbdeb02c63be.png)

2. Setting up Project ID by running 
gcloud config set project tcb-gcp-aws-007
![image](https://user-images.githubusercontent.com/52160164/129613483-e04160c3-fce8-4d53-9254-000bdbc5afcc.png)

3. Run command to setup project ID in Terraform.tfvars file
./gcp_set_project.sh
![image](https://user-images.githubusercontent.com/52160164/129613720-200ec424-a41f-45e4-808d-a021c479586a.png)

4. Validate the Project name by checking the terraform.tfvars file
cat /home/ankurjainoistgcp/hands-on-tcb-bmc-gcp/terraform/terraform.tfvars
![image](https://user-images.githubusercontent.com/52160164/129614098-8315aa72-53f2-4b0e-910c-c6d167db651c.png)

**Generating a Key Pairs**

1. Run below command to create new SSH key to access VM
ssh-keygen -t rsa -f ~/.ssh/vm-ssh-key -C ankurjainoistgcp
![image](https://user-images.githubusercontent.com/52160164/129614730-5ad5b84e-8046-4f21-bc79-9488f8bc7c04.png)

2. Set up permission for private key
chmod 400 ~/.ssh/vm-ssh-key
![image](https://user-images.githubusercontent.com/52160164/129614839-7d9272f4-cb82-42a7-844e-4436dfa5d792.png)

**Importing Public Key to GCP**

1. Run below command and this will add the key to SSH Keys to the compute engine/Metadata
gcloud compute config-ssh --ssh-key-file=~/.ssh/vm-ssh-key
![image](https://user-images.githubusercontent.com/52160164/129615511-2bbc5243-c4c4-47bd-a41a-0db319190dbb.png)

**Importing Public Key to AWS**
1. Download the public key from Google CLoud SHell 
/home/ankurjainoistgcp/.ssh/vm-ssh-key.pub
![image](https://user-images.githubusercontent.com/52160164/129616448-b628e48f-1bc7-4c88-ab9d-ccf053e9e882.png)

2. Create KeyPair in AWS 
![image](https://user-images.githubusercontent.com/52160164/129617064-1315989b-9681-4bad-b057-8dc845005f40.png)



