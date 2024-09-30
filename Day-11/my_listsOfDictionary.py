ec2_instance_info = [
  {
    "id": "instance-01",
    "type": "t2.macro" 
  },
  {
    "id": "instance-02",
    "type": "t3.medium" 
  },
  {
    "id": "instance-03",
    "type": "t2.xlarge" 
  }
]

print(ec2_instance_info[2]["type"])