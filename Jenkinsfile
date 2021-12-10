pipeline {
    agent {
        docker {  image 'qnib/pytest'}
    }
    stages {
        stage('Test') {
            steps {
                sh 'virtualenv venv && . venv/bin/activate'
                sh 'apt-get update && apt-get -y install python3-pip && pip3 install behave && pip3 install behave2cucumber && pip3 install behave-html-formatter && pip3 install urllib3 && pip3 install loguru && behave -D rp_enable=True -D step_based=True --tags=ODBC'
                
            }
        }
    }
}
