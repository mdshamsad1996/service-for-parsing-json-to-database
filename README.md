Assignmnet to for below task
Task:
Make a sample  service which takes the following json from an endpoint as input, parses it
and puts it into the database.
1. Input: The input will have a fixed format. The application should expect similar json
which will be posted as a content body to the endpoint.
2. Output: The output should be a number of rows that are filled in the database or error in
case of failures.
3. Add build.sh which sets up your project
4. Add run.sh which takes care of running your service on localhost:8080


#### First install docker and start service on amazon linux machine using below command

     sudo yum install docker -y
     sudo service docker start
#### Install docker compose using below command

   a. Install docker compose
   ```
   sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
   ```
   b. For Permission

   ```
   sudo chmod +x /usr/local/bin/docker-compose
   ```
   c. Create a symbolic link
   ```
   ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
   ```
  check docker-compose --version
  ```
  docker-compose --version
  ```
Once Infra label work is done, we can follow below steps to run project

Steps:
a) run below command

```sh build.sh```

this commannd will create two docker images , can check with command docker images
     
  b) run below command
  
    ```sh run.sh```
    
this command will create the container

#### Run linter using below command
```
sh source_code/scripts/lint.sh
```
