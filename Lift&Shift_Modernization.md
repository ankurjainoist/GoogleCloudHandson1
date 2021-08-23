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


**# Modernization Steps**

1. Create GKE Cluster using gcloud command

**gcloud container clusters create app-01 --project=$DEVSHELL_PROJECT_ID --zone=us-west1-a --machine-type n1-standard-4 --cluster-version=1.19.12 
--release-channel=stable --image-type ubuntu --num-nodes 1 --enable-stackdriver-kubernetes 
--subnetwork "projects/$DEVSHELL_PROJECT_ID/regions/us-west1/subnetworks/default"**


![image](https://user-images.githubusercontent.com/52160164/130496475-6339cce9-a29d-450c-9e84-8ae612329dac.png)

2. Installing the **Migrate for Anthos**

Create service account

**gcloud iam service-accounts create tcb-m4a-install \
> --project=$DEVSHELL_PROJECT_ID**

![image](https://user-images.githubusercontent.com/52160164/130496917-017dce84-b1e7-4716-b617-ee5b31c1ee3b.png)

Assign storage admin role to service account just created

**gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \--member="serviceAccount:tcb-m4a-install@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com" \--role="roles/storage.admin"**

![image](https://user-images.githubusercontent.com/52160164/130497192-4fed721f-a4d1-4a1d-9ae1-997807ecc5b0.png)

Create and download the keys of the service account

**gcloud iam service-accounts keys create tcb-m4a-install.json \--iam-account=tcb-m4a-install@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com \--project=$DEVSHELL_PROJECT_ID
**
![image](https://user-images.githubusercontent.com/52160164/130497420-ff57a3fb-5c8f-4087-80b0-098c65049131.png)

Connecting to Kubernetes Cluster

**gcloud container clusters get-credentials app-01 \--zone us-west1-a --project $DEVSHELL_PROJECT_ID**

Cluster now created

![image](https://user-images.githubusercontent.com/52160164/130497584-d49b643e-6eef-42f0-949c-a7bb43e886b9.png)

![image](https://user-images.githubusercontent.com/52160164/130497686-537caff6-d0bf-4617-8268-8ffc77efd1bc.png)


Setting up **Migrate for Anthos** components in **GKE Cluster app-01**

**migctl setup install --json-key=tcb-m4a-install.json**

![image](https://user-images.githubusercontent.com/52160164/130498468-60dcae13-4781-4dcb-ac9d-1285b9f94e7b.png)

Run **'migctl doctor'** command to validate **'Migrate for Anthos'** installation

![image](https://user-images.githubusercontent.com/52160164/130499421-58f08496-fcae-4996-a800-facf7da2ab23.png)

# **STEPS for VM Migration**

Creating service account 

**gcloud iam service-accounts create tcb-m4a-ce-src \--project=$DEVSHELL_PROJECT_ID**

![image](https://user-images.githubusercontent.com/52160164/130499921-b91b54a4-7fd7-46fc-ab8e-ca6dd5aada96.png)

Assign role **compute.viewer** and **compute.storageAdmin** to service account

**gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \--member="serviceAccount:tcb-m4a-ce-src@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com" \--role="roles/compute.viewer"
**

![image](https://user-images.githubusercontent.com/52160164/130500188-b508262f-6c34-45e7-9149-32fbe23b15e0.png)

**gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \--member="serviceAccount:tcb-m4a-ce-src@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com" \--role="roles/compute.storageAdmin"
**

Creating and Downloading the Service Account Key for above service account

**gcloud iam service-accounts keys create tcb-m4a-ce-src.json \--iam-account=tcb-m4a-ce-src@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com \--project=$DEVSHELL_PROJECT_ID
**

![image](https://user-images.githubusercontent.com/52160164/130500541-3c43781d-c4f3-49b1-8adf-56305ebf4e00.png)

Defining Compute Engine (CE) as Source

**migctl source create ce app-01-source --project $DEVSHELL_PROJECT_ID \--json-key=tcb-m4a-ce-src.json**

![image](https://user-images.githubusercontent.com/52160164/130500894-2087ee17-8cad-42a0-b562-0843ef681666.png)

# **Creating/Downloading and Checking the Migration Plan**

Source name: **app-01-source**

Creating the migration plan

**migctl migration create my-migration --source app-01-source \--vm-id app-01 --intent Image**

![image](https://user-images.githubusercontent.com/52160164/130501362-e16b6c17-9f56-4b5f-b4af-5568dc661871.png)

Checking the migration status

![image](https://user-images.githubusercontent.com/52160164/130501473-d440f055-9608-47b3-963b-7eef5d9cbdf8.png)

**(Optional)** We can download the migration plan by using below command

![image](https://user-images.githubusercontent.com/52160164/130501648-dc7beaa7-46d5-4ede-8259-8f5ac91e68ac.png)

**(Optional)** If want to edit , use **vi my-migration.yaml** command and to update the migration plan run below command

**migctl migration update my-migration --file my-migration.yaml**

Migrating the VM using migration Plan

**migctl migration generate-artifacts my-migration**

![image](https://user-images.githubusercontent.com/52160164/130502374-0d7ef59e-a65c-4333-a652-f033bfb7ab93.png)

Check the status 

**migctl migration status my-migration**

![image](https://user-images.githubusercontent.com/52160164/130502808-f464bbdd-f1ff-47b8-ba19-ca032c57bae8.png)


# **Steps to deploy the migrated workload**

Download the artifacts

![image](https://user-images.githubusercontent.com/52160164/130502922-a5fe41a8-b0d1-4427-96ac-109b8bf0e63a.png)

![image](https://user-images.githubusercontent.com/52160164/130503224-1df432e6-1bb3-4136-9b9f-964c15cce94b.png)

Open the **deployment_spec.yaml** file and add below lines in green

![image](https://user-images.githubusercontent.com/52160164/130503385-4ccecec2-b43b-475b-9e51-3ccfa0552329.png)

![image](https://user-images.githubusercontent.com/52160164/130503901-b09f97e8-f03a-47f7-aaf1-42c7bf634c89.png)

_apiVersion: v1
kind: Service
metadata:
   name: talent-management-portal
spec:
  selector:
     app: app-01
  ports:
     - protocol: TCP
       port: 80
       targetPort: 80
  type: LoadBalancer_

Now apply the change and deploy the workload

**kubectl apply -f deployment_spec.yaml**

![image](https://user-images.githubusercontent.com/52160164/130504983-e8d866a9-bf77-4e16-811d-5652993c003f.png)

Checking the external IP

**kubectl get service talent-management-portal**

![image](https://user-images.githubusercontent.com/52160164/130506235-4803ca47-bc7a-412a-9b45-e56a0d1cb5eb.png)

And open the external IP on new TAB

![image](https://user-images.githubusercontent.com/52160164/130507069-ffa544cd-ec12-4f3d-b928-f8f858a1da62.png)



























