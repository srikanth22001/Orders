node {
	stage('Checkout') { 
        git credentialsId: 'a49e32fa-98e6-434d-a42c-1bf83babfae5', url: 'https://github.com/srikanth22001/Orders.git', branch: 'master'
	}
	stage('UploadToS3') {
	    withAWS(credentials: '9383da7b-fad1-49a3-8286-90b6373aee27', region: 'us-east-1') {
            s3Upload acl: 'Private', bucket: 'test-lambda-functions1', file: './testGetOrderPythonCaller-a9020af6-a3c4-4169-a131-c2313f5bff86.zip'
            s3Upload acl: 'Private', bucket: 'test-lambda-functions1', file: './testGetOrderPython-bbaf38e3-a023-4986-b824-30635f4238f9.zip'
            s3Upload acl: 'Private', bucket: 'test-lambda-functions1', file: './testOrderCreationPyhton-d2f34216-7c70-42dc-a1f5-f16da16b07c5.zip'
        }
	}
	
    stage('Approval') {
        echo "Will deploy to ${BUILD_URL}"
   	    mail body: "Please go to URL:${BUILD_URL}", subject: "Job ${JOB_NAME} is waiting for input", to: 'testapps22001@gmail.com'
   	    input ('Do you  want to Approve this Deployment?')
    
    
   stage('Deploy') {
        withAWS(credentials: '9383da7b-fad1-49a3-8286-90b6373aee27', region: 'us-east-1') {
            def outputs = cfnUpdate(stack:'GetOrders', file:'./lambda_getorders_py_zip.yml', timeoutInMinutes:5)
        }
   }
}
