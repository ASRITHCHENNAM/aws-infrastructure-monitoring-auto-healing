# 🚀 Infrastructure Monitoring and Auto-Healing in Production

## 📌 Project Overview

Infrastructure Monitoring and Auto-Healing in Production is a cloud-based automation project developed using **Amazon Web Services (AWS)**. The project continuously monitors the health of cloud infrastructure and automatically recovers failed resources without requiring manual intervention.

The primary objective of this project is to improve infrastructure availability, reduce downtime, and minimize operational effort by leveraging AWS serverless and monitoring services.

This project demonstrates how modern cloud-native architectures can automatically detect failures, trigger recovery actions, and notify administrators in real time.

---

# 🎯 Project Objectives

- Monitor AWS infrastructure continuously.
- Detect unhealthy or failed EC2 instances automatically.
- Trigger automatic recovery actions using AWS Lambda.
- Minimize downtime without manual intervention.
- Improve system reliability and availability.
- Generate notifications for infrastructure events.
- Demonstrate serverless automation using AWS services.

---

# 🏗️ Architecture

The project follows an event-driven architecture.
<img width="2380" height="1780" alt="ec2_autoheal_architecture" src="https://github.com/user-attachments/assets/d22ea782-4d53-4582-86c0-c32cd9c0976c" />

---

# ☁️ AWS Services Used

| AWS Service | Purpose |
|------------|---------|
| Amazon EC2 | Hosts the production application |
| Amazon CloudWatch | Monitors instance health and performance |
| AWS Lambda | Executes auto-healing logic |
| Amazon SNS | Sends email notifications |
| IAM | Provides secure permissions |
| CloudWatch Alarms | Detects failures and triggers Lambda |

---

# ⚙️ Features

- Automated infrastructure monitoring
- Serverless auto-healing
- Event-driven architecture
- Email notifications
- CloudWatch alarm integration
- High availability
- Reduced manual intervention
- Cost-effective solution
- Easy deployment
- Scalable architecture

---

# 📂 Repository Structure

```
Infrastructure-Monitoring-and-Auto-Healing-in-Production/
│
├── Lambda-Code/
│   └── lambda_function.py
│
├── Requirements/
│   └── Project_Requirements.pdf
│
├── Output/
│   ├── Architecture.png
│   ├── CloudWatch_Alarm.png
│   ├── Lambda_Output.png
│   ├── SNS_Email.png
│   ├── EC2_Restart.png
│   └── Final_Output.png
│
├── README.md
```

*(Modify folder names if your repository structure differs.)*

---

# 🔄 Workflow

### Step 1

Launch an EC2 instance that hosts the application.

↓

### Step 2

Amazon CloudWatch continuously monitors the instance.

↓

### Step 3

If the instance becomes unhealthy or stops responding, a CloudWatch Alarm is triggered.

↓

### Step 4

The CloudWatch Alarm invokes the AWS Lambda function.

↓

### Step 5

The Lambda function automatically performs recovery actions such as:

- Restarting the EC2 instance
- Starting a stopped instance
- Logging the recovery activity

↓

### Step 6

Amazon SNS sends an email notification regarding the recovery process.

↓

### Step 7

The infrastructure becomes available again without manual intervention.

---

# 📸 Output Screenshots

The repository contains screenshots demonstrating the implementation.

## Architecture

[View Architecture](Outputs/Architecture.png)

---

## CloudWatch Alarm

[View Cloud Watch Alarm](Outputs/CloudWatch_Alarm.png)

---

## Lambda Execution

[View Lambda Execution](Outputs/Lambda_Output.png)

---

## EC2 Recovery

[View EC2 Recovery](Outputs/EC2_Restart.png)

---

## Email Notification

[View Email Notification](Outputs/SNS_Email.png)

---

## Final Output

[View Final Output](Outputs/Final_Output.png)

---

# 📝 Lambda Function

The Lambda function performs the following tasks:

- Reads CloudWatch alarm events
- Identifies the affected EC2 instance
- Initiates recovery actions
- Restarts or starts the EC2 instance
- Logs execution details
- Publishes notifications through SNS

---

# 📄 Requirements

The project requirements document is included in the repository.


[view Requirements](Requirements/Project_Requirements.md)

---

# 💡 Advantages

- Automatic failure recovery
- Reduced downtime
- Improved infrastructure reliability
- Serverless implementation
- Low operational cost
- Easy maintenance
- Scalable architecture
- Event-driven automation
- Real-time monitoring

---

# 🚀 Future Enhancements

- Auto Scaling Group integration
- Slack notifications
- Microsoft Teams notifications
- Multi-region deployment
- CloudFormation automation
- Terraform deployment
- AWS Systems Manager integration
- AI-based predictive failure detection
- Dashboard using Amazon QuickSight
- Cost optimization reporting

---

# 🔐 Security Considerations

- IAM Least Privilege Principle
- Secure Lambda execution role
- CloudWatch logging enabled
- SNS email verification
- Encrypted communication
- Proper IAM policies

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- AWS Cloud
- Amazon EC2
- Amazon CloudWatch
- AWS Lambda
- Amazon SNS
- IAM Roles and Policies
- Event-driven Architecture
- Infrastructure Automation
- Production Monitoring
- Auto-Healing Systems
- Serverless Computing

---

# 🛠️ Prerequisites

- AWS Account
- Basic AWS Knowledge
- IAM Permissions
- Amazon EC2
- AWS Lambda
- CloudWatch
- SNS
- Python (for Lambda Function)

---

# 👨‍💻 Author

**Asrith Chennam**

B.Tech – Artificial Intelligence and Data Science

KL University, Vijayawada

GitHub: [ASRITHCHENNAM](https://github.com/ASRITHCHENNAM)

LinkedIn: *[Asrith Chennam](https://www.linkedin.com/in/asrith-chennam/)*

---

# ⭐ If you found this project helpful

Please consider giving this repository a ⭐ on GitHub.

It motivates me to build more cloud and DevOps projects.

---

## 📜 License

This project is created for educational and learning purposes.
