**Challenge1:** <br />
**Requirement:** <br />
As a Cloud Specialist in a Company that uses Google Cloud Services, your task is to query inside Google Cloud Architecture quickly and efficiently. Your query should fetch all the VM's inside GCP. 
![image](https://user-images.githubusercontent.com/52160164/129404250-0a5dfd3c-1b11-48e2-b4b7-8ddf498aa149.png)

**Prerequisites:**<br />

1. Install Python latest version and Google SDK on your local machine. Also google API python libraries	<br />	
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
![image](https://user-images.githubusercontent.com/52160164/129407212-5b70870f-85ba-4dfd-9f7e-d8254e539da0.png)

													
2. **Setup service account** in GCP Account using IAM service. Grant **Compute Admin role** access to service account in same project on which you want to fire python query.	<br />	
 **Download the Service Account keys in JSON** to your local machine. <br />	 
![image](https://user-images.githubusercontent.com/52160164/129446072-c13bd3ff-7ecc-43d0-bf96-38f81fc1b533.png)


3. Create short [Python script](https://github.com/ankurjainoist/GoogleCloudHandson1/blob/dab31f352d35063d089c4720e7c96c1a7e5b40d9/instance_list.py) to fetch all storage buckets in GCP account   
![image](https://user-images.githubusercontent.com/52160164/129446118-ad33fc46-a290-4252-9c5b-1316f3773be7.png)


4. Run the script and display the results. <br />	
![image](https://user-images.githubusercontent.com/52160164/129446085-b99a4f89-0f46-4194-b2c5-4d4ba28c5270.png)




