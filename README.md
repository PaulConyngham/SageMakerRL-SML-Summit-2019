This workshop builds on top of the [Sagemaker Examples](https://github.com/awslabs/amazon-sagemaker-examples) to show you how, using AWS, you can parallelize the training of your reinforcment learning algorithms to get insanely fast turn around times & results for your reinforcement learning experiments.

# Instructions

## Configure the AWS CLI!

This guide assumes your have the AWS Command line interface (CLI) installed. For information on installing the CLI on your system OSx/Windows/Linux etc, head on over to this link:
[Install AWS's CLI on your system](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

1. Configure the AWS client by typing in your terminal: `aws configure`
2. for access key id: enter YOUR aws access key id, it should look something like this example `ABICWAYMZF78SDVKGPX9D`
3. for secret access key: enter YOUR aws secret access key, it should look something like this example `FkF8dVIwMUZLdMgwerSvKzeqrLeqvSuwyy23enedc`
4. for default region name select: `ap-northeast-1`
5. for default output format: press enter


## Step 0 - Cloud Formation Installation

Once you have the CLI installed, setting up this lab is as easy as running the following command in your terminal:

`aws cloudformation create-stack --stack-name awsRLSummit2019 --template-body https://s3-ap-southeast-2.amazonaws.com/aws-summit-2019-rl/AWS-summit_RL-CloudFormation.yml --capabilities CAPABILITY_IAM`



## Step 1 - Login to Sagemaker
&nbsp;
![aws console](images/awsconsole2.png)

&nbsp;

1. Login to AWS Console
2. Click "Find Services"
3. Type "SageMaker" and hit enter




## Step 2 - open our Notebook instance

&nbsp;


1. On the left menu under the "Notebook" section, click "Notebook instances"
&nbsp;
![menu](images/awssagemakerhome.png)
&nbsp;
2. Next to our instance named "amazon-RL-lab" there is a link called "open jupyter", click it.
&nbsp;
![menu](images/openjupyter.png)
&nbsp;
3. A new tab will launch taking you to a jupyter notebook. Once this has finished loading, click the link titled "Summit-RL"
4. Clicking the link will take you to a new directory. Click the file titled **"Sagemaker_RL_Lab_Summit_2019_One_Click.ipynb"** to get started with the lab!
