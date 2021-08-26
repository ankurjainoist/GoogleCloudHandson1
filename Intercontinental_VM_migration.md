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

**cd bootcamp-gcp-storage-clinic-mib-app**



























