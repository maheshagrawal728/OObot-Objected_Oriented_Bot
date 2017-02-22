# Instructions to deploy the service

In provision.yml file in OObot/Deploy/, the following things have to be filled up to deploy the service succesffuly:
- aws_access_key
- aws_secret_key
- SLACK_BOT_TOKEN
- BOT_ID
- GITHUBTOKEN


### After filling provision.yml, Run the following code to deploy

    sudo ansible-playbook -s provision.yml

Also, we use a Githb Organisation (OOBOT) in github.ncsu.edu to store all pattern. In order to be able to execute the use cases successfully, the user has to be a part of this OOBOT organisation. Kindly contact rchandh@ncsu.edu to get added into the organisation.

