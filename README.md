# Event Driven Microservices

### Stack: Django, Flask, Docker, RabbitMQ, MySQL.  

----------------------  

The app is divided into 2 main Microservices:  

- Admin Services built with Django, Docker, MySQL:  

  - You can perform CRUD operation on Product using APIs built with Django REST.  
  - Products are delivered to RabbitMQ via Producer.  
  
   
  
- Main app built with Flask, Docker, MySQL:  

  - Flask gets products from RabbitMQ via consumer.  
  - You can Like Products using the Flask APP.  
  
![diagram](https://user-images.githubusercontent.com/73492002/182219050-71557077-350e-4d31-b52d-a53c5e88948c.PNG)


