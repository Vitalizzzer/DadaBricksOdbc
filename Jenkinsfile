pipeline {
    agent {
        docker {  image '3.6/alpine3.15'}
    }
    stages {
        stage('Test') {
            steps {
                sh 'virtualenv venv && . venv/bin/activate'
                sh 'apt-get update'                
                sh 'apt-get -y install python3-pip'
                sh 'pip3 install behave'
                sh 'pip3 install behave2cucumber'
                sh 'pip3 install behave-html-formatter'
                sh ' pip3 install reportportal-behave-client-custom'
                sh 'behave -D rp_enable=True -D step_based=True --tags=ODBC'
               
                
            }
        }
    }
}
