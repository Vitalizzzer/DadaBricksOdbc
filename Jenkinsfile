pipeline {
    agent none
    stages {
        stage('Build') {
             agent {
                docker {  image 'python:2-alpine'}
            }
            steps {
              //  sh 'python -m py_compile '
                //sh 'virtualenv venv && . venv/bin/activate'
               // sh 'apt-get update'                
               // sh 'apt-get -y install python3-pip'
                 sh 'pip3 install behave'
//                 sh 'pip3 install behave2cucumber'
//                 sh 'pip3 install behave-html-formatter'
//                 sh 'pip3 install reportportal-behave-client-custom'
                 sh 'behave -D rp_enable=True -D step_based=True --tags=ODBC'
               
                
            }
        }
    }
}
