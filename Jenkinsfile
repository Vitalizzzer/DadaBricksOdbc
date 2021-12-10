pipeline {
    agent {
        docker {  image 'qnib/pytest'}
    }
    stages {
        stage('Test') {
            steps {
                sh 'virtualenv venv && . venv/bin/activate && pip install behave && behave -f html -o report/cucumber_report.html -D rp_enable=True -D step_based=True --tags=ODBC'
                
            }
        }
    }
}
