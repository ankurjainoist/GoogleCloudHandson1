**# Requirement**

As Cloud Specialist now task is to implement the automation of talent onboarding web application in order that the Human Talent Analyst can create a user just using form page.

Some task needed in mission are
1. Set up Webservice plugin in Moodle
2. Deploy Backend using Cloud Function service
3. Deploy Frontend using the Cloud Storage service to host the static web application files. 

![image](https://user-images.githubusercontent.com/52160164/132564939-c413de89-aa04-44f9-9a51-7b7fc116709a.png)

![image](https://user-images.githubusercontent.com/52160164/132565279-7c01c60e-57ed-4fdb-a9a1-4b08abbb60fd.png)

![image](https://user-images.githubusercontent.com/52160164/132938057-113a55ca-7504-4477-b832-14cca5c9f2dc.png)

![image](https://user-images.githubusercontent.com/52160164/132938067-55cf6072-8c52-458e-8895-0e6d8102e9a8.png)

![image](https://user-images.githubusercontent.com/52160164/132941102-d187fe10-91cc-4f74-8cf9-d5059ee0260e.png)

Download the Python code

wget https://storage.googleapis.com/bootcamp-gcp-en/bootcamp-gcp-final-project.zip

unzip bootcamp-gcp-final-project.zip

![image](https://user-images.githubusercontent.com/52160164/132941133-704359bc-d71b-4291-869b-f6a9d94a5013.png)

![image](https://user-images.githubusercontent.com/52160164/132941141-7979fee4-c249-4694-b431-07b1a17ff93f.png)

TRigger URL of cloud function

https://us-central1-prod-project-83573.cloudfunctions.net/moodleUserCreate

After triggering the URL with data user gets created

curl -X POST -F 'inputName=Jean' -F 'inputLastname=Rodrigues' -F 'inputEmail=jeanrodrigues123@gmail.com'  https://us-central1-prod-project-83573.cloudfunctions.net/moodleUserCreate

![image](https://user-images.githubusercontent.com/52160164/132941482-21282c9c-36e3-4c34-998d-8cbad9f144a7.png)

it failed for the first time due to 403 Forbidden error and so added below member with cloud invoke role access

![image](https://user-images.githubusercontent.com/52160164/132941517-bae955b7-c500-4f67-b129-6b3ea38acb3a.png)

**# Setting up the Frontend**

Using the Cloud Editor, edit the file **~/bootcamp-gcp-final-project/frontend/index.html** In the action, replace the info to the Trigger URL

![image](https://user-images.githubusercontent.com/52160164/132941655-b7de3850-045b-4d79-b8a3-291d93f83c86.png)

Create Bucket in Cloud storage via cloud shell

gsutil mb gs://tcb-gl-onb-ankur

![image](https://user-images.githubusercontent.com/52160164/132941769-cb8f12d2-4e60-4bf9-a8b0-2a147817a1cb.png)

Uploading the front end files to bucket created

cd ~/bootcamp-gcp-final-project/frontend/

**gsutil cp * gs://tcb-gl-onb-ankur**

![image](https://user-images.githubusercontent.com/52160164/132941836-5109072b-e612-481a-a045-6a6ef9fd9282.png)

**Setting up the bucket **

**gsutil web set -m index.html -e 404.html gs://tcb-gl-onb-ankur**
  
**gsutil iam ch allUsers:objectViewer gs://tcb-gl-onb-ankur**

![image](https://user-images.githubusercontent.com/52160164/132941897-86e2b00e-0448-442b-a8cc-051e05c83988.png)

![image](https://user-images.githubusercontent.com/52160164/132941911-e32ab1ea-ad61-4196-98bf-3937ab2b90d7.png)

![image](https://user-images.githubusercontent.com/52160164/132941938-9708ee2a-4565-483d-9554-1e26b70381e8.png)

Portal is accessible 

![image](https://user-images.githubusercontent.com/52160164/132941952-664a74a0-dbe4-404d-bdc3-4c068ec29675.png)


