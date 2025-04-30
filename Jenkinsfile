pipeline {
    agent any

    environment {
        PIP = '/usr/bin/pip3'
        PYTHON = '/usr/bin/python3'  // 실제 경로로 바꿔줘요.
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'git', url: 'https://github.com/dayeDev/jenkins_test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh "${PIP} install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                sh "${PYTHON} -m pytest tests"
            }
        }
    }
}
