pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git credentialsId: 'git', url: 'https://github.com/dayeDev/jenkins_test.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }
}
