pipeline {
    agent {
        docker {  image 'qnib/pytest'}
    }
    stages {
        stage('Test') {
            steps {
                sh 'virtualenv venv && . venv/bin/activate && pip install behave'
            }
        }
    }
}
