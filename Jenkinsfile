pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'git', url: 'https://github.com/dayeDev/jenkins_test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    export PATH="/usr/bin:$PATH"
                    /usr/bin/pip3 install --upgrade pip
                    /usr/bin/pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    export PATH="/usr/bin:$PATH"
                    /usr/bin/python3 -m pytest tests
                '''
            }
        }
    }
}
