**Project 1 HandsOn:** <br />
**Requirement:** <br />
As a Cloud Specialist in a Company that uses Google Cloud Services, your task is to query inside Google Cloud Architecture quickly and efficiently. Your query should fetch all the storage buckets inside GCP. 
![image](https://user-images.githubusercontent.com/52160164/129404250-0a5dfd3c-1b11-48e2-b4b7-8ddf498aa149.png)

**Prerequisites:**<br />

1. Install Python latest version and Google SDK on your local machine. Also install python libraries for GCP Storage services 	<br />	
![image](https://user-images.githubusercontent.com/52160164/129404644-dcf13df8-1f9a-4609-83e4-4222446a3546.png)
pip3 install --upgrade google-cloud-storage
![image](https://user-images.githubusercontent.com/52160164/129405110-ae79d80d-872e-4ae2-8abe-864b7db23946.png)

													
2. **Setup service account** in GCP Account using IAM service. Grant **Storage Admin role** access to service account. **Download the Service Account keys in JSON** to your local machine. <br />	 
![image](https://user-images.githubusercontent.com/52160164/129404748-50ddcea8-5850-4bb2-957a-f6a27dfc5144.png)

3. Create short [Python script](https://github.com/ankurjainoist/GoogleCloudHandson1/blob/806cbb4a051405b5e5c3cfde6b86eca74fa9f895/storage_list.py) to fetch all storage buckets in GCP account   
![image](https://user-images.githubusercontent.com/52160164/129405129-4bcecb62-09ff-473a-a8a9-8594f3e4940a.png)

4. Run the script and display the results. <br />	
![image](https://user-images.githubusercontent.com/52160164/129405180-ab260d60-8343-426c-a790-7b3b27279340.png)



