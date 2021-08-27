# **Requirement:**

**As a cloud specialist, your task is to migrate an application + database in an intercontinental environment (US Region->Australia) in a totally private way, 
using the Infrastructure of GCP. Once the application and database are properly working in the US region, based on the knowledge of GCP's Storage services, 
you decide to deploy this migration to Australia using the Storage Snapshots feature to migrate both data and settings of the VMs, Safely and quickly!**

![image](https://user-images.githubusercontent.com/52160164/131011350-2763e56b-c947-45f5-9794-cc27d35cd2dc.png)

**Steps:**

1. Create two instances APP and DB in GCP for application and database hosting

**gcloud compute instances create usa-app01 --machine-type e2-micro --zone us-west1-b** 

**gcloud compute instances create usa-db01 --machine-type e2-micro --zone us-west1-b **

![image](https://user-images.githubusercontent.com/52160164/131012792-f22ff0e4-8126-4745-9f1b-9eb16e75948a.png)

2. Open SSH port of both instances and run below commands 

# **Setting up DB VM**

**sudo apt update** 

**sudo apt-get -y install wget**

**wget http://repo.mysql.com/mysql-apt-config_0.8.13-1_all.deb**

![image](https://user-images.githubusercontent.com/52160164/131013489-6ec541fe-5bcc-4d9f-93e2-93882eb63266.png)

![image](https://user-images.githubusercontent.com/52160164/131013618-da1b839a-383c-421a-b11a-e9171a41128e.png)

![image](https://user-images.githubusercontent.com/52160164/131013940-1b5b0cd0-1402-4f77-a29e-888627bfee0e.png)

**sudo dpkg -i mysql-apt-config_0.8.13-1_all.deb**

![image](https://user-images.githubusercontent.com/52160164/131014115-dc918fda-6628-4bda-9327-e89ce8f03b58.png)

![image](https://user-images.githubusercontent.com/52160164/131014336-9e148c1e-919f-4f8e-8ddc-1d41192594a9.png)

# **Install MySQL Server**

**sudo apt update

**sudo apt install mysql-server -y**

![image](https://user-images.githubusercontent.com/52160164/131014566-5d2378d5-85d1-4be2-a5b4-70728d351334.png)

**Select default authentication plugin**

**SelectUse Legacy Authentication Method (Retain MySQL 5.x Compatibility)**

![image](https://user-images.githubusercontent.com/52160164/131014626-ae0e3262-7487-4f13-9da9-280c0ca7b85b.png)

![image](https://user-images.githubusercontent.com/52160164/131014849-d030f73b-3cf1-4255-b261-7084c4e0dd98.png)

**Restart the MySQL service**

**sudo systemctl restart mysql.service**

**Setting up MySQL**

**sudo mysql_secure_installation**

Enter password and N for all questions

![image](https://user-images.githubusercontent.com/52160164/131015312-ce030e9c-74c5-4297-be63-8715b754e0e3.png)

![image](https://user-images.githubusercontent.com/52160164/131015465-5d82ef04-b904-4a89-ba7a-6db9d402817a.png)

**Download the file *.sql**

**wget https://storage.googleapis.com/bootcamp-gcp-en/bootcamp-gcp-storage-db-en.sql**

**Connect to DB**

**mysql -u root -p**

![image](https://user-images.githubusercontent.com/52160164/131015859-2d531a9e-eb8a-4778-91d2-98a871eca92a.png)

**Creating DB and Tables**

**source bootcamp-gcp-storage-db-en.sq**l

![image](https://user-images.githubusercontent.com/52160164/131015992-682074ec-b765-41ee-9e84-200f0a6c1d0e.png)

Create User and changing the privilages

**CREATE USER app@'%' IDENTIFIED BY 'welcome1';
GRANT ALL PRIVILEGES ON clinic.* TO app@'%';
FLUSH PRIVILEGES; 
exit**

![image](https://user-images.githubusercontent.com/52160164/131016755-a490a718-a0e1-46e1-b3c6-6e243c6ad26b.png)


# **Setting up App VM for the application **

**sudo apt-get update**

**sudo apt-get install -y npm**

**sudo apt-get install -y zip**

**sudo apt-get install -y wget**

**wget https://storage.googleapis.com/bootcamp-gcp-en/bootcamp-gcp-storage-clinic-mid-app.zip**

![image](https://user-images.githubusercontent.com/52160164/131020600-67fa2744-6cb0-478f-931c-426f4e6f2b62.png)

**unzip bootcamp-gcp-storage-clinic-mid-app.zip**

**cd bootcamp-gcp-storage-clinic-mid-app**

![image](https://user-images.githubusercontent.com/52160164/131141190-4fbe96ab-5948-4d9b-88db-e57e94c00619.png)

**Edit the file **

From the folder bootcamp-gcp-storage-clinic-mid-app,
run the following command to edit the file **index.js**

**nano src/index.js**

![image](https://user-images.githubusercontent.com/52160164/131141500-63e9cee0-c913-4514-a6d4-74a6f8002266.png)

Inside file, in the middleware section replace

**host:to the Private IP address of the database VM.**

**user:to app,**

**password: to welcome1**

**database:to clinic**

![image](https://user-images.githubusercontent.com/52160164/131142108-e0283702-7fa9-4819-8748-69ac3236b671.png)

Now run the command, to install the NPM package inside the folder

**npm install**

![image](https://user-images.githubusercontent.com/52160164/131142326-14053eac-a94e-44a7-a402-4401eb6c1d66.png)

# **Start the node.js application**

**node src/index.js**

![image](https://user-images.githubusercontent.com/52160164/131142583-18cbd2ef-c9dc-4a7a-99c8-64b73f7b0ff3.png)

Default port for node.js is 3000 and as we have not allowed traffic in this port it will not open anything.

Create the firewall rule to allow the TCP access on 3000 port, go to FIREWALL service in GCP portal and create new firewall rule

![image](https://user-images.githubusercontent.com/52160164/131142857-131355a3-27e0-4a86-acbd-f18f54c1f426.png)

![image](https://user-images.githubusercontent.com/52160164/131143162-e4fe34c5-460b-4884-83aa-3215cdfe1530.png)

![image](https://user-images.githubusercontent.com/52160164/131143121-6611a96d-0339-48bd-9106-0285ff855c4f.png)

Node JS application now started on port 3000

http://35.203.190.66:3000/

![image](https://user-images.githubusercontent.com/52160164/131153964-6651c475-a884-47dc-a6c2-db6ba932a08d.png)


# **Now migrating the VM's using the Storage Snapshot**

1. Create SNAPSHOT from disks of the VM's db-app01(DB VM) and usa-app01 (App VM)

**gcloud compute disks snapshot db-app01 --snapshot-names usa-db01-snapshot --zone us-west1-b**

**gcloud compute disks snapshot usa-app01 --snapshot-names usa-app01-snapshot --zone us-west1-b**

![image](https://user-images.githubusercontent.com/52160164/131158226-bf7c60ea-9b47-4528-8fcb-a28263c06b79.png)

Snapshots Created

![image](https://user-images.githubusercontent.com/52160164/131158316-5a9982d2-354f-4534-b54d-8fd8be7e7b19.png)

2. Create disks in Autralia Region australia-southeast1 using source as the above created snapshots created in US region

**gcloud compute disks create aus-db01 --source-snapshot usa-db01-snapshot --zone australia-southeast1-a**

**gcloud compute disks create aus-app01 --source-snapshot usa-app01-snapshot --zone australia-southeast1-a**

![image](https://user-images.githubusercontent.com/52160164/131158795-3308e3ba-2bf5-431f-bcd5-04094368ed87.png)

Australia Disk created

![image](https://user-images.githubusercontent.com/52160164/131158873-d58da1d5-734e-4a09-afce-ef0615137bd9.png)

3. Now creating instances in Sydney region, using source as the Disks created in previous step

**gcloud compute instances create aus-app01 --machine-type e2-micro --zone australia-southeast1-a --disk name=aus-app01,boot=yes,mode=rw**

**gcloud compute instances create aus-db01 --machine-type e2-micro --zone australia-southeast1-a --disk name=aus-db01,boot=yes,mode=rw**

![image](https://user-images.githubusercontent.com/52160164/131159219-a1ff5a3b-c8aa-4428-9193-7a88f74bc267.png)

Instances created

![image](https://user-images.githubusercontent.com/52160164/131159270-288f7ef5-ad22-4b69-87b0-9fb146927fc9.png)

4. Access aus-app01 via SSH and open folder of app

![image](https://user-images.githubusercontent.com/52160164/131159485-60570255-27b1-4d23-9088-a57c6c3165ad.png)

5. Edit index file and change Private IP of aus-db01

**nano src/index.js**

![image](https://user-images.githubusercontent.com/52160164/131159845-a7b6ed6c-9fa6-4a78-9ba6-ce0a4c3b658a.png)

6. Start the node js application and access the application via port 3000 in browser

![image](https://user-images.githubusercontent.com/52160164/131160020-c0359096-cfdd-46a1-a613-9db44bb79ccf.png)

App opened in Aus region now **http://<external-ip-from-aus-app01:3000**

![image](https://user-images.githubusercontent.com/52160164/131160134-c17790d3-26aa-4be8-996e-aec74df67e6b.png)















































