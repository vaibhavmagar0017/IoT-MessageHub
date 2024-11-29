# **IoT-MessageHub**

A Python-based project that integrates MQTT messaging via RabbitMQ and stores messages in MongoDB. It also includes a FastAPI-based endpoint to query message status counts within a specified time range.

---

## **Features**
- Publishes MQTT messages every second with a random `status` (0–6) via RabbitMQ.
- Consumes and stores messages in MongoDB for analysis.
- Provides a REST API endpoint to retrieve message status counts based on a time range.

---

## **Installation & Setup**

### **1. Clone the Repository**
- git clone https://github.com/vaibhavmagar0017/IoT-MessageHub.git
- cd IoT-MessageHub

### **2. Install Dependencies**
- pip install -r requirements.txt

### **3. Switch to the `develop` Branch**
```bash
git checkout develop
git pull origin
```

---

## **Set Up RabbitMQ**  
(*Skip this step if RabbitMQ is already set up.*)

### **1. Install RabbitMQ**
```bash
sudo apt update
sudo apt install rabbitmq-server -y
```

### **2. Enable MQTT Plugin**
```bash
sudo rabbitmq-plugins enable rabbitmq_mqtt
sudo systemctl restart rabbitmq-server
```

### **3. Start and Check RabbitMQ**
```bash
sudo systemctl start rabbitmq-server
sudo systemctl status rabbitmq-server
```

### **4. Verify RabbitMQ Port (5672)**
Check if RabbitMQ is running on the default port:
```bash
telnet localhost 5672
```

### **5. Check RabbitMQ Logs**
Monitor RabbitMQ logs for any issues:
```bash
sudo tail -f /var/log/rabbitmq/rabbit@$(hostname).log
```

### **6. Allow Port 5672 in Firewall**
```bash
sudo ufw allow 5672
```

### **7. (Optional) Create a RabbitMQ User**
Create a new user with permissions:
```bash
sudo rabbitmqctl add_user testuser testpassword
sudo rabbitmqctl set_permissions -p / testuser ".*" ".*" ".*"
```

### **8. Update Credentials in `client.py`**
Modify the connection settings in `client.py` if a custom RabbitMQ user is created.

---

## **Run Services**

### **1. Start the Client**
Publishes MQTT messages to RabbitMQ:
```bash
python client.py
```

### **2. Start the Server**
Consumes messages from RabbitMQ and stores them in MongoDB:
```bash
python server.py
```

### **3. Start the FastAPI App**
Starts the API to query message status counts:
```bash
uvicorn app:app --reload
```

### **4. Test the Endpoint**
Query message status counts using the following curl command:
```bash
curl "http://127.0.0.1:8000/status_count/?start_time=0&end_time=9999999999"
```

## **Notes**
- Ensure RabbitMQ and MongoDB services are running before starting the client, server, or FastAPI app.
- The `start_time` and `end_time` values for the API endpoint must be Unix timestamps.
- Customize the `client.py` and `server.py` as needed for specific configurations.
