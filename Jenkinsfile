pipeline {
    agent any

    environment {
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
                sh "${PYTHON} -m venv venv"
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest tests'
            }
        }
    }
}
