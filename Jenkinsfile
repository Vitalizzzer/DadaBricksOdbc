pipeline {
  stages {
    stage('Test') {
         agent {
              docker {
                   image 'qnib/pytest'
              }
         }
         steps {
              sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python tests.py'
         }
    }
  }
}

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
