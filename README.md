# TheHive-SideProjects
A Slack webhook I created using Flask

Big shout out to Eric and everyone at [Recon InfoSec](https://reconinfosec.com/)

# Requirements
1. Linux server requirements 

    * `sudo apt-get update && sudo apt-get -y upgrade`

    * `sudo apt-get install python-pip`

    * `sudo pip install flask`

    * `sudo pip install request`

    * `sudo pip install requests`

1. Add the following environmental variables:

    * `export hookURL=https://hooks.slack.com/services/<yourslackwebhook>`
    
    * `export hiveURL=https://yourhiveserver.com or IP`
    
        * note: You might have to edit your `.bashrc` or `.profile` to add your variables

1. Configure your Hive server to send webhooks to Flask

1. $PROFIT

# Caution!

1. Make sure you change your `crypto secret` on TheHive [(source)](https://github.com/TheHive-Project/TheHiveDocs/blob/master/admin/configuration.md)
1. Make sure you configure SSL and a Proxy if you use in production [(source)](https://github.com/TheHive-Project/TheHiveDocs/blob/master/admin/webhook.md)
1. I used the Flask builtin development server for TESTING ONLY. Please change it if you will use this in production[(source)](https://github.com/TheHive-Project/TheHiveDocs/blob/master/installation/binary-guide.md)
    * I recommend [Gunicorn](http://gunicorn.org/) with [NGINX](https://www.nginx.com/). You have lots of [choices](http://flask.pocoo.org/docs/0.12/deploying/)
    * Better yet, get with the times and go [serverless](https://github.com/ReconInfoSec/thehive-slack-webhook)

# Contributors

* [@cyberGoatPsyOps](https://twitter.com/cyberGoatPsyOps)
* [@eric_capuano](https://twitter.com/eric_capuano)
* And of course everyone at [TheHive Project](https://github.com/TheHive-Project/TheHive)
